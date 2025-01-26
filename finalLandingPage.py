import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import newdatabase



class SignUp():
    
    def authenticate_user(self) :
        username = self.user.entry1.get()
        password = self.password.entry2.get()
        userdata = newdatabase.db.authenticate_user(username, password)
        '''newdatabase.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        userdata = newdatabase .cursor.fetchone()'''
        if userdata :
            self.landingpage()
        else : 
            messagebox.showerror("Error", "Invalid username or password")
        #self.landingpage()

    def landingpage(self) :
        self.user.destroy()
        self.user.entry1.destroy()
        self.password.destroy()
        self.password.entry2.destroy()
        self.button.destroy()
        self.rbutton.destroy()

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

    def __init__(self,tkob):
        self.tkob = tkob
        self.login_img = Image.open('loginpage_bgr.png')
        self.login_img = self.login_img.resize((950, 650))
        self.login_img = ImageTk.PhotoImage(self.login_img)

        self.l_img = Label(tkob, image=self.login_img)
        self.l_img.place(x=0, y=0)


        self.lg = Label(tkob, text="Login Here", font=('Comic Sans MS', 30, 'bold'))
        self.lg.place(x=380, y=10)


        self.user = Label(tkob, text = "Username" , font = ("Ariel", 15, "bold"))
        self.user.place(x =265, y = 125)
        self.user.entry1 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.user.entry1.place(x = 415, y = 125)

        self.password = Label(tkob, text = "Password", font = ("Ariel", 15, "bold"))
        self.password.place(x = 265, y = 185)
        self.password.entry2 = Entry(tkob, font = ("Ariel",15, "bold"))
        self.password.entry2.place(x = 415, y = 185)
        self.password.entry2.bind("<KeyRelease>", self.display_password)

        self.button = Button(tkob, text = "Login", font = ("Ariel", 15, "bold"), command = self.authenticate_user)
        self.button.place(x = 290, y = 275)

        self.rbutton = Button(tkob, text = "Register", font = ("Ariel", 15, "bold"), command = self.registerpage)
        self.rbutton.place(x = 500, y = 275)

        self.fbutton = Button(tkob, text = "Forgot Password", font = ("Ariel", 15, "bold"), command = self.change)
        self.fbutton.place(x = 360, y = 380)



class Register() :

    def add_user(self) :
        user_name = self.username.en1.get()
        e_mail = self.email.en2.get()
        pass_word = self.password.en3.get()
        mob_ile = self.mobile.en4.get()
        newdatabase.db.add_user(user_name, e_mail, pass_word, mob_ile)
    

    def register(self) :
        self.add_user()
        self.R.destroy()
        self.username.destroy()
        self.username.en1.destroy()
        self.email.destroy()
        self.email.en2.destroy()
        self.password.destroy()
        self.password.en3.destroy()
        self.mobile.destroy()
        self.mobile.en4.destroy()
        self.rbutton.destroy()

        l_page = Landing_page(tkob)

    def backPage(self) :
        self.username.destroy()
        self.username.en1.destroy()
        self.email.destroy()
        self.email.en2.destroy()
        self.password.destroy()
        self.password.en3.destroy()
        self.mobile.destroy()
        self.mobile.en4.destroy()
        self.rbutton.destroy()


        s_page = SignUp(tkob)

    def display_password(self, event) :
        self.password.en3.config(show = ".")


    def __init__(self, tkob) :
        self.tkob = tkob
        self.sign_img = Image.open('loginpage_bgr.png')
        self.sign_img = self.sign_img.resize((950, 650))
        self.sign_img = ImageTk.PhotoImage(self.sign_img)

        self.s_img = Label(tkob, image=self.sign_img)
        self.s_img.place(x=0, y=0)

        self.R = Label(tkob, text="Register Yourself", font=('Comic Sans MS', 30, 'bold'))
        self.R.place(x=350, y=10)

        self.username = Label(tkob, text = "UserName", font = ("Ariel", 15, "bold"))
        self.username.place(x = 275, y = 150)
        self.username.en1 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.username.en1.place(x = 500, y = 150)

        self.email = Label(tkob, text = "Email", font = ("Ariel", 15, "bold"))
        self.email.place(x = 275, y = 200)
        self.email.en2 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.email.en2.place(x = 500, y = 200)



        self.password = Label(tkob, text = "Password", font = ("Ariel", 15, "bold"))
        self.password.place(x = 275, y = 250)
        self.password.en3 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.password.en3.place(x = 500, y = 250)
        self.password.en3.bind("<KeyRelease>", self.display_password)


        self.mobile = Label(tkob, text = "Mobile No", font = ("Ariel", 15, "bold"))
        self.mobile.place(x = 275, y = 300)
        self.mobile.en4 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.mobile.en4.place(x = 500, y = 300)

        self.rbutton = Button(tkob, text = "Create an Account", font = ("Ariel", 15, "bold"), command = self.register)
        self.rbutton.place(x = 400, y = 400)

        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.backPage)
        self.back_button.place(x = 10, y = 10)


class ChangePassword() :

    def change_password(self) :
        new_password = self.new_password.p1.get()
        email = self.mail.m1.get()
        newdatabase.update_password(new_password, email)

    def display(self, event) :
        self.new_password.p1.config(show = ".")
    
    def check_email(self) :
        mail = self.mail.m1.get()
        newdatabase.cursor.execute("SELECT * FROM users WHERE email = ?", (mail,))
        userdata = newdatabase .cursor.fetchone()
        if userdata :
            self.change_password()
            sign = SignUp(tkob)
        else : 
            messagebox.showerror("Error","Email doesn't exist")

    
    def back_page(self) :
        self.L.destroy()
        self.mail.destroy()
        self.mail.m1.destroy()
        self.new_password.destroy()
        self.new_password.p1.destroy()
        self.change.destroy()
        self.bg_label.destroy()

        #change_password_page = ChangePassword(self.tkob)
        go_back = SignUp(tkob)



    def __init__(self, tkob) :
        self.tkob = tkob
        self.forgot_img = Image.open('loginpage_bgr.png')
        self.forgot_img = self.forgot_img.resize((950, 650))
        self.forgot_img = ImageTk.PhotoImage(self.forgot_img)


        ##Adding changes
        self.bg_label = tk.Label(tkob, image = self.forgot_img)
        self.bg_label.image = self.forgot_img
        self.bg_label.place(x = 0, y = 0)

        self.L = Label(tkob, text="Change Password", font=('Comic Sans MS', 30, 'bold'))
        self.L.place(x=350, y=10)

        self.mail = Label(tkob, text = "Email", font = ("Ariel", 15, "bold"))
        self.mail.place(x = 275, y = 200)
        self.mail.m1 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.mail.m1.place(x = 500, y = 200)

        self.new_password = Label(tkob, text = "New Password", font = ("Ariel", 15, "bold"))
        self.new_password.place(x = 275, y = 250)
        self.new_password.p1 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.new_password.p1.place(x = 500, y = 250)
        self.new_password.p1.bind("<KeyRelease>", self.display)

        self.change = Button(tkob, text = "Confirm Password", font = ("Ariel", 15, "bold"), command = self.check_email)
        self.change.place(x = 400, y = 350)

        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.back_page)
        self.back_button.place(x = 10, y = 10)

        


class Landing_page():
    
    def next_page(self):
        skintype = self.skin_type_dropdown.get()
        skinconcern = self.skin_concern_dropdown.get()

        self.name.destroy()
        self.tag.destroy()
        self.bg_img.destroy()
        self.skin_type_label.destroy()
        self.skin_type_dropdown.destroy()
        self.skin_concern_label.destroy()
        self.skin_concern_dropdown.destroy()
        self.suggest.destroy()
        self.back_button.destroy()

        sug = Suggest(tkob, skintype, skinconcern)

    def signup(self) :
        self.name.destroy()
        self.tag.destroy()
        self.bg_img.destroy()
        self.skin_type_label.destroy()
        self.skin_type_dropdown.destroy()
        self.skin_concern_label.destroy()
        self.skin_concern_dropdown.destroy()
        self.suggest.destroy()
        self.back_button.destroy()

        sign = SignUp(tkob)

    def __init__(self, tkob):
        self.tkob = tkob
        self.bgr_img = Image.open('bgr_img.png')
        self.bgr_img = self.bgr_img.resize((950, 650))
        self.bgr_img = ImageTk.PhotoImage(self.bgr_img)

        self.bg_img = Label(tkob, image=self.bgr_img)
        self.bg_img.place(x=0, y=0)

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

class Suggest():
    def backpage(self) :
        #self.bg2_img.destroy()
        self.label.destroy()
        #self.frame1.destroy()
        self.frame_main.destroy()
        '''self.ingredients_frame.destroy()
        self.ingredients_title.destroy()
        self.ingredients_content.destroy()
        self.tips_frame.destroy()
        self.tips_title.destroy()
        self.tips_content.destroy()
        self.frame2.destroy()
        self.textbox1.destroy()
        self.textbox2.destroy()
        self.back_button.destroy()'''
        #started
        #self.bg2_img.destroy()
        #self.label.destroy()
        self.frame_main.destroy()
        self.back_button.destroy()

        landing = Landing_page(tkob)


    def __init__(self,tkob, skintype, skinconcern):
        self.tkob = tkob
        self.skintype = skintype
        self.skinconcern = skinconcern

        def pro_tip(skintype) :
            if skintype == "oily" :
                List = ["Use clay mask", "Be gentle and don't over exfoliate"]
            elif skintype == "combination":
                List = ["Use spot treatment", "Adjust skincare routine seasonally"]
            elif skintype == "normal" :
                List = ["Focus on hydration and sun protection", "Avoid harsh products"]
            elif skintype == "dry" :
                List = ["Be gentle and don't over exfoliate", "Focus on skin barrier", "Apply moisturizer on damp skin"]
            elif skintype == "sensitive" :
                List = ["Use minimal products", "Focus on skin barrier"]
            elif skintype == "aging" :
                List = ["Don't skip sunscreen", "Switch to healthy lifestyle"]

            return List
            

        def get_ingredient(user_skintype, user_concern) :
            #newdatabase.cursor.execute(f"SELECT concerns.ingredient FROM concerns JOIN skintypes ON concerns.ingredient = skintypes.ingredient WHERE concern = '{user_concern}' AND skintype = '{user_skintype}' ")
            ingredients = newdatabase.db.get_ingredients_by_type_and_concern(user_skintype, user_concern) #fetching single result
            print(ingredients)
            return [ingredient for ingredient in ingredients]
    
        '''self.bgr2_img = Image.open('con_bgr.png')
        self.bgr2_img = self.bgr2_img.resize((950, 650))
        self.bgr2_img = ImageTk.PhotoImage(self.bgr2_img)

        self.bg2_img = Label(tkob, image=self.bgr2_img)
        ##Keeping reference
        self.bg2_img.image = self.bgr2_img
        self.bg2_img.place(x = 0, y = 0)'''
        
        ##started
        # Main background color
        tkob.configure(bg = "#F2F6FF")
        # Main frame with improved layout
        self.frame_main = tk.Frame(tkob, bg="#E8F0FE", padx=30, pady=20)
        self.frame_main.pack(expand=True, fill=tk.BOTH, padx = 10, pady = 10)
        
        # Personalized title with improved styling
        self.label = tk.Label(
            self.frame_main, 
            text="Your Personalized Skincare Guide", 
            font=("Roman", 20, "bold"), 
            fg="#3C4F76", 
            bg="#E8F0FE"
        )
        self.label.pack(pady=(0, 20))
        
        # Ingredients Section
        ingredients_frame = tk.Frame(self.frame_main, bg="#DCEBFF", relief = tk.GROOVE, borderwidth = 2, padx = 10, pady = 10)
        ingredients_frame.pack(fill=tk.X, pady=10)

        ingredients_title = tk.Label(
            ingredients_frame, 
            text="Recommended Ingredients", 
            font=("Helvetica", 18, "bold"), 
            fg="#2C3E50", 
            bg="#DCEBFF"
        )
        ingredients_title.pack(pady=(0, 10))
        
        ingredients_content = tk.Text(
            ingredients_frame, 
            height=10, 
            width=50, 
            font=("Arial", 12), 
            bg="#F7F9F9", 
            fg="#2C3E50",
            borderwidth=1, 
            relief="solid",
            padx=10,
            pady=10
        )
        
        ingredients_content.tag_configure("header", font=("Helvetica", 14, "bold"))
        ingredients_content.insert(tk.END, f"Skin Type: {self.skintype}\n", "header")
        ingredients_content.insert(tk.END, f"Skin Concern: {self.skinconcern}\n\n", "header")
        
        ingredients = get_ingredient(self.skintype, self.skinconcern)
        for ingredient in ingredients:
            ingredients_content.insert(tk.END, f"• {ingredient}\n")
        
        ingredients_content.config(state=tk.DISABLED)  # Make read-only
        ingredients_content.pack(fill=tk.X)
        
        # Pro Tips Section
        tips_frame = tk.Frame(self.frame_main, bg="#FFEFD5", relief = tk.GROOVE, borderwidth = 2, padx = 10, pady = 10)
        tips_frame.pack(fill=tk.X, pady=10)

        tips_title = tk.Label(
            tips_frame, 
            text="Pro Tips", 
            font=("Helvetica", 18, "bold"), 
            fg="#2C3E50", 
            bg="#FFEFD5"
        )
        tips_title.pack(pady=(0, 10))
        
        tips_content = tk.Text(
            tips_frame, 
            height=5, 
            width=50, 
            font=("Arial", 12), 
            bg="#F0F4F8", 
            fg="#2C3E50",
            borderwidth=1, 
            relief="solid",
            padx=10,
            pady=10
        )
        tips_content.tag_configure("tip", font=("Helvetica", 12))
        
        protips = pro_tip(self.skintype)
        for protip in protips:
            tips_content.insert(tk.END, f'\U0001F4A1 {protip}\n', "tip")
        
        tips_content.config(state=tk.DISABLED)  # Make read-only
        tips_content.pack(fill=tk.X)

        # Back Button with improved styling
        self.back_button = Button(
            tkob, 
            text="\u2B05", 
            font=("Arial", 15, "bold"), 
            bg="#E0E0E0", 
            fg="#3C4F76", 
            relief=tk.RAISED, 
            command=self.backpage
        )
        self.back_button.place(x=10, y=10)
        
        
        
        
        
        
        
        
        
        
        

        '''self.label = tk.Label(tkob, text = "Here's is your personalized skin care ingredients", font = ("Roman", 20, "bold"), bg = "white")
        self.label.pack(pady = 20) 

        self.frame1 = tk.Frame(tkob, bg = "white")
        self.frame1.pack(side = tk.TOP)

        self.frame2 = tk.Frame(tkob, bg = "white")
        self.frame2.pack(side = tk.BOTTOM)

        # Create a Text widget
        #self.textlabel = tk.Label(tkob, text = )
        self.textbox1 = tk.Text(self.frame1, height=15, width=30, bg = "white")
        ingredients = get_ingredient(self.skintype, self.skinconcern)
        self.textbox1.insert(tk.END, "skin Type : " + self.skintype + "\n" + "Skin Concern : " + self.skinconcern + "\n" + "\n", "bold")
        for ingredient in ingredients :
            self.textbox1.insert(tk.END, ingredient + "\n")
        self.textbox1.pack(padx = 20, pady = 30)


        self.textbox2 = tk.Text(self.frame2, height=7, width=300, bg = "white")
        self.textbox2.insert(tk.END, "Pro Tips \n")  # Insert text at the center top
        self.textbox2.tag_add("center", "1.0", "1.end")
        self.textbox2.tag_configure("center", justify="center")
        self.textbox2.insert(tk.END, "\n", "bold")
        protips = pro_tip(self.skintype)
        for protip in protips :
            self.textbox2.insert(tk.END, '\U0001F4A1' + protip + "\n")
        self.textbox2.pack(padx=20, pady=30)  
        

        

        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.backpage)
        self.back_button.place(x = 10, y = 10)'''



tkob = tk.Tk()
tkob.title("Glow Genius")
tkob.iconbitmap('icon.ico')
signup = SignUp(tkob)
tkob.geometry('950x650+250+30')
tkob.resizable(False,False)
#landing_page = Landing_page(tkob)
tkob.mainloop()


