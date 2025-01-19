import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import database
from newModel import test_model, train_skincare_model

## import the dependencies for using hugging face's BART model
import os
from pathlib import Path
from transformers import pipeline
from transformers import BartTokenizer, BartForConditionalGeneration
import torch


class CustomStyles:
    # Custom colors
    PRIMARY_COLOR = "#6B46C1"  # Purple
    SECONDARY_COLOR = "#F3E8FF"  # Light purple
    TEXT_COLOR = "#2D3748"  # Dark gray
    BUTTON_HOVER_COLOR = "#553C9A"  # Darker purple
    
    # Custom styles
    TITLE_FONT = ("Helvetica", 32, "bold")
    SUBTITLE_FONT = ("Helvetica", 14, "italic")
    LABEL_FONT = ("Helvetica", 12, "bold")
    BUTTON_FONT = ("Helvetica", 12, "bold")
    
    @staticmethod
    def style_button(button):
        button.configure(
            bg=CustomStyles.PRIMARY_COLOR,
            fg="white",
            font=CustomStyles.BUTTON_FONT,
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        
    @staticmethod
    def style_entry(entry):
        entry.configure(
            font=("Helvetica", 11),
            relief=tk.SOLID,
            bd=1
        )
        
    @staticmethod
    def setup_hover_effect(button):
        def on_enter(e):
            button['background'] = CustomStyles.BUTTON_HOVER_COLOR
            
        def on_leave(e):
            button['background'] = CustomStyles.PRIMARY_COLOR
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)




class SignUp():
    def __init__(self, tkob):
        self.tkob = tkob
        self.setup_background()
        self.create_widgets()
        self.style_widgets()
        
    def setup_background(self):
        # Create a gradient effect
        self.canvas = tk.Canvas(self.tkob, width=950, height=650)
        self.canvas.place(x=0, y=0)
        self.canvas.lower
        
        # Create gradient
        for i in range(650):
            color = '#{:02x}{:02x}{:02x}'.format(
                107 - int(i/650*20),
                70 - int(i/650*20),
                193 - int(i/650*20)
            )
            self.canvas.create_line(0, i, 950, i, fill=color)
            
        # Add decorative elements
        self.canvas.create_oval(-50, -50, 150, 150, fill="#7C3AED", outline="")
        self.canvas.create_oval(850, 550, 1000, 700, fill="#7C3AED", outline="")
        
    
    def create_widgets(self):
        # Create a frame for the login form
        self.login_frame = tk.Frame(
            self.tkob,
            bg="white",
            relief=tk.SOLID,
            bd=1
        )
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=500, height=450)
        
        # Title
        self.lg = Label(
            self.login_frame,
            text="Welcome Back!",
            font=CustomStyles.TITLE_FONT,
            bg="white",
            fg=CustomStyles.PRIMARY_COLOR
        )
        self.lg.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
         # Username
        self.user = Label(
            self.login_frame,
            text="Username",
            font=CustomStyles.LABEL_FONT,
            bg="white",
            fg=CustomStyles.TEXT_COLOR
        )
        self.user.place(x=50, y=100)
        
        self.user.entry1 = Entry(self.login_frame, width=25)
        self.user.entry1.place(x=50, y=130)
        CustomStyles.style_entry(self.user.entry1)
        
        # Password
        self.password = Label(
            self.login_frame,
            text="Password",
            font=CustomStyles.LABEL_FONT,
            bg="white",
            fg=CustomStyles.TEXT_COLOR
        )
        self.password.place(x=50, y=170)
        
        self.password.entry2 = Entry(self.login_frame, width=25, show="•")
        self.password.entry2.place(x=50, y=200)
        CustomStyles.style_entry(self.password.entry2)
        
        # Buttons
        self.button = Button(
            self.login_frame,
            text="Login",
            command=self.authenticate_user
        )
        self.button.place(relx=0.5, rely=0.6, anchor=tk.CENTER, width=200)
        
        self.rbutton = Button(
            self.login_frame,
            text="Create Account",
            command=self.registerpage
        )
        self.rbutton.place(relx=0.5, rely=0.7, anchor=tk.CENTER, width=200)
        
        self.fbutton = Button(
            self.login_frame,
            text="Forgot Password?",
            command=self.change
        )
        self.fbutton.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=200)
        
    def style_widgets(self):
        # Style all buttons
        for button in [self.button, self.rbutton, self.fbutton]:
            CustomStyles.style_button(button)
            CustomStyles.setup_hover_effect(button)
            
    def authenticate_user(self):
        username = self.user.entry1.get()
        password = self.password.entry2.get()
        if database.db.authenticate_user(username, password):
            self.landingpage()
        else:
            messagebox.showerror("Error", "Invalid username or password")
            
            
    
    def landingpage(self) :
        self.login_frame.destroy()
        self.lg.destroy()
        self.user.destroy()
        self.user.entry1.destroy()
        self.password.destroy()
        self.password.entry2.destroy()
        self.button.destroy()
        self.rbutton.destroy()
        self.fbutton.destroy()

        landing_page = Landing_page(tkob)

    def registerpage(self) :
        self.user.destroy()
        self.user.entry1.destroy()
        self.password.destroy()
        self.password.entry2.destroy()
        self.button.destroy()
        self.rbutton.destroy()
        self.fbutton.destroy()

        register_page = Register(tkob)

    def display_password(self, event) :
        self.password.entry2.config(show = ".") 

    def change(self) :
        self.lg.destroy()
        self.user.destroy()
        self.user.entry1.destroy()
        self.password.destroy()
        self.password.entry2.destroy()
        self.button.destroy()
        self.rbutton.destroy()
        self.fbutton.destroy()

        new_password_page = ChangePassword(tkob)



            
class Landing_page():
    
    def next_page(self):
        skintype = self.skin_type_dropdown.get()
        skinconcern = self.skin_concern_dropdown.get()

        self.name.destroy()
        self.tag.destroy()
        #self.bg_img.destroy()
        self.skin_type_label.destroy()
        self.skin_type_dropdown.destroy()
        self.skin_concern_label.destroy()
        self.skin_concern_dropdown.destroy()
        self.suggest.destroy()
        #self.back_button.destroy()

        sug = Suggest(tkob, skintype, skinconcern)

    def signup(self) :
        self.name.destroy()
        self.tag.destroy()
        #self.bg_img.destroy()
        self.skin_type_label.destroy()
        self.skin_type_dropdown.destroy()
        self.skin_concern_label.destroy()
        self.skin_concern_dropdown.destroy()
        self.suggest.destroy()
        self.back_button.destroy()

        sign = SignUp(tkob)

    def __init__(self, tkob):
        self.tkob = tkob
        '''self.bgr_img = Image.open('bgr_img.png')
        self.bgr_img = self.bgr_img.resize((950, 650))
        self.bgr_img = ImageTk.PhotoImage(self.bgr_img)

        self.bg_img = Label(tkob, image=self.bgr_img)
        self.bg_img.place(x=0, y=0)'''

        self.name = Label(tkob, text="Glow Genius", font=('Roman', 50, 'bold'))
        self.name.place(x=300, y=10)
        
        self.tag = Label(tkob, text = " - get the best version of your skin..", font = ('Courier New' ,13))
        self.tag.place(x=550, y=100)

        self.skin_type_label = Label(tkob, text="Skin Type:", font=('Courier New', 15, 'bold'))
        self.skin_type_label.place(x=85, y=180)

        
        self.skin_type_dropdown = ttk.Combobox(tkob, font=('Courier New', 10) )
        self.skin_type_dropdown['values'] = ['normal', 'dry', 'oily','sensitive','combination', 'aging'] 
        self.skin_type_dropdown.place(x=215, y=180)
  
        self.skin_concern_label = Label(tkob, text="Skin Concern:", font=('Courier New', 15,'bold'))
        self.skin_concern_label.place(x=500, y=180)

        self.skin_concern_dropdown = ttk.Combobox(tkob, font=('Courier New', 10))
        self.skin_concern_dropdown['values'] = ['acne', 'hyperpigmentation', 'uneven texture', 'eczema', 'melasma', 'enlarged pores','dark circles', 'None']
        self.skin_concern_dropdown.place(x=665, y=180)

        self.suggest = Button(tkob,text = "Suggest" , font = ('Times New Roman',15,'bold'),command = self.next_page)
        self.suggest.place(x = 425 , y = 300)

        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.signup)
        self.back_button.place(x = 10, y = 10)
     
     
       
            
            
class Register():
    def __init__(self, tkob):
        self.tkob = tkob
        self.setup_background()
        self.create_widgets()
        self.style_widgets()
        
        
    def register(self) :
        self.add_user()
        self.R.destroy()
        self.username.destroy()
        self.username.entry.destroy()
        self.email.destroy()
        self.email.entry.destroy()
        self.password.destroy()
        self.password.entry.destroy()
        self.mobile.destroy()
        self.mobile.entry.destroy()
        self.rbutton.destroy()

        l_page = Landing_page(tkob)

    def backPage(self) :
        self.username.destroy()
        self.username.entry.destroy()
        self.email.destroy()
        self.email.entry.destroy()
        self.password.destroy()
        self.password.entry.destroy()
        self.mobile.destroy()
        self.mobile.entry.destroy()
        self.rbutton.destroy()


        s_page = SignUp(tkob)

    def display_password(self, event) :
        self.password.entry.config(show = ".")

        
    def setup_background(self):
        # Similar gradient background as SignUp
        self.canvas = tk.Canvas(self.tkob, width=950, height=650)
        self.canvas.place(x=0, y=0)
        
        for i in range(650):
            color = '#{:02x}{:02x}{:02x}'.format(
                107 - int(i/650*20),
                70 - int(i/650*20),
                193 - int(i/650*20)
            )
            self.canvas.create_line(0, i, 950, i, fill=color)
            
    def create_widgets(self):
        # Create a frame for registration form
        self.register_frame = tk.Frame(
            self.tkob,
            bg="white",
            relief=tk.SOLID,
            bd=1
        )
        self.register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=500, height=550)
        
        # Title
        self.R = Label(
            self.register_frame,
            text="Create Account",
            font=CustomStyles.TITLE_FONT,
            bg="white",
            fg=CustomStyles.PRIMARY_COLOR
        )
        self.R.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        # Form fields
        fields = [
            ("UserName", "username"),
            ("Email", "email"),
            ("Password", "password"),
            ("Mobile No", "mobile")
        ]
        
        for i, (label_text, attr) in enumerate(fields):
            label = Label(
                self.register_frame,
                text=label_text,
                font=CustomStyles.LABEL_FONT,
                bg="white",
                fg=CustomStyles.TEXT_COLOR
            )
            label.place(x=50, y=100 + i*70)
            
            entry = Entry(self.register_frame, width=30)
            entry.place(x=50, y=130 + i*70)
            CustomStyles.style_entry(entry)
            
            setattr(self, attr, label)
            setattr(getattr(self, attr), 'entry', entry)
        
        # Buttons
        self.rbutton = Button(
            self.register_frame,
            text="Create Account",
            command=self.register
        )
        self.rbutton.place(relx=0.5, rely=0.85, anchor=tk.CENTER, width=200)
        
        self.back_button = Button(
            self.register_frame,
            text="←",
            command=self.backPage
        )
        self.back_button.place(x=20, y=20)
        
    def style_widgets(self):
        CustomStyles.style_button(self.rbutton)
        CustomStyles.setup_hover_effect(self.rbutton)
        CustomStyles.style_button(self.back_button)
        CustomStyles.setup_hover_effect(self.back_button)
        
        
    def add_user(self):
        username = self.username.entry.get()
        email = self.email.entry.get()
        password = self.password.entry.get()
        mobile = self.mobile.entry.get()
        if database.db.add_user(username, email, password, mobile):
            self.R.destroy()
            self.username.destroy()
            self.username.entry.destroy()
            self.email.destroy()
            self.email.entry.destroy()
            self.password.destroy()
            self.password.entry.destroy()
            self.mobile.destroy()
            self.mobile.entry.destroy()
            self.rbutton.destroy()
        
            l_page = Landing_page(tkob)
        else:
            messagebox.showerror("Error", "Username or email already exists")
            
 
 
 
 
class ChangePassword() :
    
    def change_password(self) :
        new_password = self.new_password.p1.get()
        email = self.mail.m1.get()
        database.db.update_password(email, new_password)

    def display(self, event) :
        self.new_password.p1.config(show = ".")
    
    def check_email(self):
        email = self.mail.m1.get()
        if database.db.check_email_exists(email):
            self.change_password()
            sign = SignUp(tkob)
        else:
            messagebox.showerror("Error", "Email doesn't exist") 
        
    
    def back_page(self) :
        self.L.destroy()
        self.mail.destroy()
        self.mail.m1.destroy()
        self.new_password.destroy()
        self.new_password.p1.destroy()
        self.change.destroy()

        #change_password_page = ChangePassword(self.tkob)
        go_back = SignUp(tkob)



    def __init__(self, tkob) :
        self.tkob = tkob
        '''self.forgot_img = Image.open('loginpage_bgr.png')
        self.forgot_img = self.forgot_img.resize((950, 650))
        self.forgot_img = ImageTk.PhotoImage(self.forgot_img)


        ##Adding changes
        self.bg_label = tk.Label(tkob, image = self.forgot_img)
        self.bg_label.image = self.forgot_img
        self.bg_label.place(x = 0, y = 0)'''

        self.L = Label(tkob, text="Change Password", font=('Comic Sans MS', 30, 'bold'))
        self.L.place(x=300, y=10)

        self.mail = Label(tkob, text = "Email", font = ("Ariel", 15, "bold"))
        self.mail.place(x = 270, y = 200)
        self.mail.m1 = Entry(tkob, font = ("Ariel", 15, "bold"), bg = "lightgray", relief = "solid", bd = 2)
        self.mail.m1.place(x = 465, y = 200)

        self.new_password = Label(tkob, text = "New Password", font = ("Ariel", 15, "bold"))
        self.new_password.place(x = 270, y = 250)
        self.new_password.p1 = Entry(tkob, font = ("Ariel", 15, "bold"), bg = "lightgray", relief = "solid", bd = 2)
        self.new_password.p1.place(x = 465, y = 250)
        self.new_password.p1.bind("<KeyRelease>", self.display)

        self.change = Button(tkob, text = "Confirm Password", font = ("Ariel", 15, "bold"), command = self.check_email)
        self.change.place(x = 400, y = 350)

        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.back_page)
        self.back_button.place(x = 10, y = 10)
    



class Suggest() :
    def __init__(self, tkob, skintype, skinconcern):
        self.tkob = tkob
        self.skintype = skintype
        self.skinconcern = skinconcern
        
        custom_path = 'D:/wise/ModelCache/bart-large'
        # Add local_files_only=False to force download if files don't exist
        try:
            self.tokenizer = BartTokenizer.from_pretrained(
                "facebook/bart-large", cache_dir=custom_path
                #cache_dir=str(cache_dir),
                #froce_download = True
                #local_files_only=False
            )
            print('Tokenizer downloaded')
            
            self.model = BartForConditionalGeneration.from_pretrained(
                "facebook/bart-large",
                cache_dir=custom_path
                #cache_dir=str(cache_dir),
                #froce_download = True
                #cache_dir=custom_path,
                #local_files_only=False
            )
            print('Model downloaded')
        except Exception as e:
            print(f"Error during model loading: {str(e)}")
        
        # Get ingredients
        #skintype_ingredients = database.db.get_ingredients_by_type(skintype)
        #concern_ingredients = database.db.get_ingredients_by_concern(skinconcern)
        
        # Combine ingredients (remove duplicates)
        #self.ingredients = list(set(skintype + skinconcern)) 
        
        # This will hod the generated recommendations
        self.recommendations = self.generate_skincare_recommendations() 
        self.display_recommendations(self.recommendations)
        '''try :
            self.recommendations = self.generate_skincare_recommendations() 
            self.display_recommendations(self.recommendations)
        except Exception as e :
            messagebox.showerror("Error", f"failed to generate recommendations")'''
            
    def format_output(self, raw_output) :
        items = [item.strip() for item in raw_output.split(",") if item.strip()]
        return list(dict.fromkeys(items))
        
    def generate_skincare_recommendations(self):
        '''# process the input for the skin type and skin concern
        input_text = f"Suggest skincare ingredients to make skin healthy for skin type: {self.skintype} and skin concern: {self.skinconcern}"
        inputs = self.tokenizer.encode(input_text, return_tensors='pt')
        
        # Generate recommendations using BART model
        with torch.no_grad():
            output = self.model.generate(inputs, max_length=150, num_beams=5, early_stopping=True)
        
        # Decode the output
        decoded_output = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return decoded_output'''
        input_text = f"Recommend ingredients for skin type: {self.skintype} and skin concern: {self.skinconcern}"
        raw_output = test_model(model, tokenizer, input_text)
        formatted_output = self.format_output(raw_output)
        return formatted_output
        #return test_model(model, tokenizer, input_text)


    def display_recommendations(self, recommendations):
        # Display the generated ingredient suggestions in the GUI
        self.result_label = Label(self.tkob, text="Recommended Ingredients")
        self.result_label.pack()
        
        #if isinstance(recommendations, list) :
            #recommendations = "\n".join(f". {item}" for item in recommendations)
            
        self.result_text = Text(self.tkob, wrap='word', width=60, height=10)
        self.result_text.pack(pady=10)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, recommendations)
        #self.result_text.pack()
        #self.result_text.delete(1.0, END)
        #self.result_text.insert(END, recommendations)

    def backpage(self) :
        #self.bg2_img.destroy()
        self.label.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.textbox1.destroy()
        self.textbox2.destroy()
        self.back_button.destroy()

        landing = Landing_page(self.tkob)   
        




tkob = tk.Tk()
tkob.title("Glow Genius")
tkob.iconbitmap('icon.ico')
signup = SignUp(tkob)
tkob.geometry('950x650+250+30')
tkob.resizable(False,False)
#landing_page = Landing_page(tkob)
# Load the trained model and tokenizer
output_dir = 'trained_skincare_model'
tokenizer = BartTokenizer.from_pretrained(output_dir)
model = BartForConditionalGeneration.from_pretrained(output_dir)
tkob.mainloop()