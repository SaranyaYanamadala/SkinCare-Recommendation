import sqlite3
conn = sqlite3.connect('mydata.db') #connect to db
cursor = conn.cursor() #cursor object to exeute SQL commands

# concerns table
cursor.execute('''
  CREATE TABLE concerns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT NOT NULL,
    concern TEXT NOT NULL
  )
''')

def add_item(ingredient, concern) :
  cursor.execute("INSERT INTO concerns (ingredient, concern) VALUES(?, ?)", (ingredient, concern))
  conn.commit()

add_item("Salicylic Acid", "acne")
add_item("Benzoyl Peroxide", "acne")
add_item("Glycolic Acid", "acne")
add_item("Retinoids (Retinol, Tretinoin)", "acne")
add_item("Sulfur", "acne")
add_item("Tea Tree Oi", "acne")
add_item("Azelaic Acid", "acne")
add_item("Niacinamide (Vitamin B3)", "acne")
add_item("Hyaluronic Acid", "acne")
add_item("Clay", "acne")
add_item("Zinc", "acne")
add_item("Witch Hazel", "acne")
add_item("Aloe Vera", "acne")
add_item("Green Tea Extract", "acne")
add_item("Lactic Acid", "acne")
add_item("Mandelic Acid", "acne")

add_item("Hydroquinone", "hyperpigmentation")
add_item("Kojic Acid", "hyperpigmentation")
add_item("Vitamin C", "hyperpigmentation")
add_item("Niacinamide", "hyperpigmentation")
add_item("Azelaic Acid", "hyperpigmentation")
add_item("Alpha Arbutin", "hyperpigmentation")
add_item("Licorice Extract", "hyperpigmentation")
add_item("Retinoids", "hyperpigmentation")
add_item("Glycolic Acid", "hyperpigmentation")
add_item("Lactic Acid", "hyperpigmentation")
add_item("Mandelic Acid", "hyperpigmentation")
add_item("Tranexamic Acid", "hyperpigmentation")
add_item("Mulberry Extract", "hyperpigmentation")
add_item("Bearberry Extract", "hyperpigmentation")
add_item("Vitamin E", "hyperpigmentation")
add_item("Ferulic Acid", "hyperpigmentation")
add_item("Resveratrol", "hyperpigmentation")
add_item("Vitamin B5", "hyperpigmentation")
add_item("Papaya Extract", "hyperpigmentation")
add_item("Turmeric Extract", "hyperpigmentation")

add_item("Retinoids","uneven texture")
add_item("Glycolic Acid","uneven texture")
add_item("Lactic Acid","uneven texture")
add_item("Salicylic Acid","uneven texture")
add_item("Mandelic Acid","uneven texture")
add_item("Azelaic Acid","uneven texture")
add_item("Vitamin C","uneven texture")
add_item("Peptides","uneven texture")
add_item("Ceramides","uneven texture")
add_item("Hyaluronic Acid","uneven texture")
add_item("Niacinamide","uneven texture")
add_item("Licorice Extract","uneven texture")
add_item("Willow Bark Extract","uneven texture")
add_item("Centella Asiatica","uneven texture")
add_item("Vitimine B5","uneven texture")
add_item("Rosehip Oil","uneven texture")
add_item("Jojoba Oil","uneven texture")

add_item("Emollients and Moisturizers", "eczema")
add_item("Ceramides", "eczema")
add_item("Oatmeal", "eczema")
add_item("Jojoba Oil", "eczema")
add_item("Licorice Extract", "eczema")
add_item("Aloe Vera", "eczema")
add_item("Chamomile Extract", "eczema")
add_item("Vitamin E", "eczema")
add_item("Zinc Oxide", "eczema")
add_item("Probiotics", "eczema")
add_item("Collodial Oatmeal", "eczema")
add_item("Panthenol", "eczema")
add_item("Mandelic Acid", "eczema")
add_item("Glycerin", "eczema")
add_item("Probiotics", "eczema")

add_item("Salicylic Acid Retinoids","enlarged pores")
add_item("Niacinamide","enlarged pores")
add_item("Glycolic Acid","enlarged pores")
add_item("Lactic Acid","enlarged pores")
add_item("Azelaic Acid","enlarged pores")
add_item("Witch Hazel","enlarged pores")
add_item("Clay","enlarged pores")
add_item("Tea Tree Oil","enlarged pores")
add_item("Vitamin C","enlarged pores")
add_item("Hyaluronic Acid","enlarged pores")
add_item("Jojoba Oil","enlarged pores")
add_item("Rosehip Oil","enlarged pores")
add_item("Licorice Extract","enlarged pores")
add_item("Centella Asiatica","enlarged pores")
add_item("Green Tea Extract","enlarged pores")
add_item("Zinc","enlarged pores")
add_item("Vitamin E","enlarged pores")

add_item("Hydroquinone","melasma")
add_item("Kojic Acid","melasma")
add_item("Azelaic Acid","melasma")
add_item("Vitamin C","melasma")
add_item("Niacinamide","melasma")
add_item("Retinoids","melasma")
add_item("Glycolic Acid","melasma")
add_item("Lactic Acid","melasma")
add_item("Mandelic Acid","melasma")
add_item("Tranexamic Acid","melasma")
add_item("Alpha Arbutin","melasma")
add_item("Licorice Extract","melasma")
add_item("Mulberry Extract","melasma")
add_item("Bearberry Extract","melasma")
add_item("Vitamin E","melasma")
add_item("Ferulic Acid","melasma")
add_item("Resveratrol","melasma")
add_item("Green Tea Extract","melasma")

add_item("Vitamin C","dark circles")
add_item("Vitamin K","dark circles")
add_item("Caffeine","dark circles")
add_item("Retinoids","dark circles")
add_item("Hyaluronic Acid","dark circles")
add_item("Peptides","dark circles")
add_item("Niacinamide","dark circles")
add_item("Arnica Extract","dark circles")
add_item("Licorice Extract","dark circles")
add_item("Kojic Acid","dark circles")
add_item("Alpha Arbutin","dark circles")
add_item("Green Tea Extract","dark circles")
add_item("Chamomile Extract","dark circles")
add_item("Cucumber Extract","dark circles")
add_item("Aloe Vera","dark circles")
add_item("Almond Oil","dark circles")
add_item("Rosehip Oil","dark circles")
add_item("Jojoba Oil","dark circles")
add_item("Shea Butter","dark circles")
add_item("Coconut Oil","dark circles")


# skin types table
cursor.execute('''
  CREATE TABLE skintypes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT NOT NULL,
    skintype TEXT NOT NULL
  )
''')

def add_ingredient(ingredient, skintype) :
  cursor.execute("INSERT INTO skintypes (ingredient, skintype) VALUES(?, ?)", (ingredient, skintype))
  conn.commit()

add_ingredient("Alpha Arbutin", "oily")
add_ingredient("Alpha Arbutin", "combination")
add_ingredient("Alpha Arbutin", "normal")
add_ingredient("Alpha Arbutin", "dry")
add_ingredient("Alpha Arbutin", "sensitive")
add_ingredient("Aloe Vera", "sensitive")
add_ingredient("Argan Oil", "dry")
add_ingredient("Argan Oil", "aging")
add_ingredient("Azelaic Acid", "oily")
add_ingredient("Bearberry Extract", "sensitive")
add_ingredient("Benzoyl Peroxide", "oily")
add_ingredient("Ceramides", "dry")
add_ingredient("Ceramides", "aging")
add_ingredient("Centella Asiatica ", "sensitive")
add_ingredient("Chamomile", "oily")
add_ingredient("Chamomile", "normal")
add_ingredient("Chamomile", "combination")
add_ingredient("Chamomile", "dry")
add_ingredient("Chamomile", "sensitive")
add_ingredient("Clay", "oily")
add_ingredient("Ferulic Acid", "aging")
add_ingredient("Glycerin", "dry")
add_ingredient("Glycolic Acid", "oily")
add_ingredient("Glycolic Acid", "combination")
add_ingredient("Glycolic Acid", "normal")
add_ingredient("Green Tea Extract", "oily")
add_ingredient("Honey", "dry")
add_ingredient("Hyaluronic Acid", "dry")
add_ingredient("Hydroquinone", "oily")
add_ingredient("Hydroquinone", "combination")
add_ingredient("Hydroquinone", "normal")
add_ingredient("Jojoba Oil", "dry")
add_ingredient("Kojic Acid", "oily")
add_ingredient("Lactic Acid", "dry")
add_ingredient("Lactic Acid", "sensitive")
add_ingredient("Licorice Extract", "sensitive")
add_ingredient("Mandelic Acid", "oily")
add_ingredient("Mandelic Acid", "combinaton")
add_ingredient("Mandelic Acid", "normal")
add_ingredient("Mandelic Acid", "dry")
add_ingredient("Mandelic Acid", "sensitive")
add_ingredient("Marula Oil", " dry")
add_ingredient("Marula Oil", "aging")
add_ingredient("Mulberry Extract", "sensitive")
add_ingredient("Niacinamide", "oily")
add_ingredient("Niacinamide", "combination")
add_ingredient("Niacinamide", "normal")
add_ingredient("Niacinamide", "dry")
add_ingredient("Niacinamide", "sensitive")
add_ingredient("Vitamin C", "oily")
add_ingredient("Vitamin C", "combination")
add_ingredient("Vitamin C", "normal")
add_ingredient("Vitamin C", "aging")
add_ingredient("Vitamin E", "dry")
add_ingredient("Vitamin E", "sensitive")
add_ingredient("Vitamin E", "aging")
add_ingredient("Zinc", "oily")
add_ingredient("Witch Hazel", "oily")
add_ingredient("Willow Bark Extract", "oily")
add_ingredient("Squalane", "dry")
add_ingredient("Squalane", "combination")
add_ingredient("Panthenol", "sensitive")
add_ingredient("Panthenol", "dry")
add_ingredient("Peptides", "aging")
add_ingredient("Bakuchiol", "aging")
add_ingredient("Coenzyme Q10", "aging")
add_ingredient("Allantoin", "sensitive")
add_ingredient("Calendula", "sensitive")
add_ingredient("Green Tea Extract", "sensitive")
add_ingredient("Salicylic Acid", "oily")
add_ingredient("AHA", "normal")
add_ingredient("AHA", "combination")
add_ingredient("Tranexamic Acid", "hyperpigmentation")
add_ingredient("Alpha Arbutin", "hyperpigmentation")
add_ingredient("Fatty Acids", "dry")
add_ingredient("Ceramides", "sensitive")
