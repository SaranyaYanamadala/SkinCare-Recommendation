import torch
from transformers import BartTokenizer, BartForConditionalGeneration, Trainer, TrainingArguments
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from sklearn.model_selection import train_test_split

class SkincareDataset(Dataset):
    def __init__(self, data, tokenizer, max_length=128):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length
        
    def __len__(self):
        """Return the number of items in the dataset"""
        return len(self.data) if isinstance(self.data, pd.DataFrame) else 0

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        
        # Improved input text formatting
        input_text = f"For {row['skin_type']} skin with {row['skin_concern']}, recommend specific skincare ingredients:"
        
        # Ensure ingredients are properly formatted in the target text
        target_text = self.format_ingredients(row['ingredients'])

        # Tokenize with improved parameters
        inputs = self.tokenizer(
            input_text,
            padding='max_length',
            truncation=True,
            max_length=self.max_length,
            return_tensors='pt'
        )

        targets = self.tokenizer(
            target_text,
            padding='max_length',
            truncation=True,
            max_length=self.max_length,
            return_tensors='pt'
        )

        return {
            'input_ids': inputs['input_ids'].squeeze(),
            'attention_mask': inputs['attention_mask'].squeeze(),
            'labels': targets['input_ids'].squeeze()
        }
    
    @staticmethod
    def format_ingredients(ingredients):
        """Format ingredients into a clear, structured list"""
        # Clean and standardize ingredient format
        if isinstance(ingredients, str):
            # Split ingredients if they're in a comma-separated string
            ingredients_list = [i.strip() for i in ingredients.split(',')]
            # Remove empty strings and duplicates while maintaining order
            ingredients_list = list(dict.fromkeys(filter(None, ingredients_list)))
            # Join with proper formatting
            return "Recommended ingredients: " + ", ".join(ingredients_list)
        return ingredients

def train_skincare_model(data_path, output_dir, num_epochs=5):
    # Load and preprocess data
    df = pd.read_csv(data_path)
    
    # Clean ingredients column (remove incomplete entries)
    df = df[df['ingredients'].str.len() > 5]  # Remove very short/empty ingredients
    
    train_df, val_df = train_test_split(df, test_size=0.1, random_state=42)
    
    # Initialize with improved configuration
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-base', ignore_mismatched_sizes = True)
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-base', ignore_mismatched_sizes = True)
    
    # Create datasets
    train_dataset = SkincareDataset(train_df, tokenizer)
    val_dataset = SkincareDataset(val_df, tokenizer)
    
    # Enhanced training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=num_epochs,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=100,
        evaluation_strategy="steps",
        eval_steps=500,
        save_steps=1000,
        load_best_model_at_end=True,
        metric_for_best_model='loss',
        greater_is_better=False,
        #generation_max_length=128,
        #generation_num_beams=4
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset
    )
    
    trainer.train()
    
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    
    return model, tokenizer

def generate_text(model, tokenizer, input_text, max_length=128):
    """Helper function for text generation with specific parameters"""
    inputs = tokenizer(input_text, return_tensors='pt', max_length=max_length, truncation=True)
    
    outputs = model.generate(
        inputs['input_ids'],
        max_length=max_length,
        num_beams=5,
        early_stopping=True,
        no_repeat_ngram_size=2,
        length_penalty=1.0,
        min_length=20,
        #temperature=0.7
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def test_model(model, tokenizer, test_input):
    model.eval()
    
    # Improve input formatting
    if not test_input.startswith("For"):
        test_input = f"For {test_input.split('skin type: ')[1]}"
    
    inputs = tokenizer(test_input, return_tensors='pt', max_length=128, truncation=True)
    
    # Improved generation parameters
    with torch.no_grad():
        outputs = model.generate(
            inputs['input_ids'],
            max_length=128,
            num_beams=5,
            early_stopping=True,
            no_repeat_ngram_size=2,
            length_penalty=1.0,
            min_length=20,
            #temperature=0.7
        )
    
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Clean up prediction
    if "Recommended ingredients:" in prediction:
        prediction = prediction.split("Recommended ingredients:")[1].strip()
    
    # Format final output
    ingredients = [ing.strip() for ing in prediction.split(',')]
    ingredients = [ing for ing in ingredients if len(ing) > 2]  # Remove very short tokens
    return ", ".join(ingredients)

if __name__ == "__main__":
    data_path = 'skincare_training_data.csv'
    output_dir = 'trained_skincare_model'
    
    model, tokenizer = train_skincare_model(data_path, output_dir)
    
    test_cases = [
        "Recommend ingredients for skin type: oily and skin concern: acne",
        "Recommend ingredients for skin type: dry and skin concern: eczema",
        "Recommend ingredients for skin type: sensitive and skin concern: hyperpigmentation"
    ]
    
    print("\nTesting model with sample inputs:")
    for test_input in test_cases:
        prediction = test_model(model, tokenizer, test_input)
        print(f"\nInput: {test_input}")
        print(f"Predicted ingredients: {prediction}")