import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
from subprocess import call

# Initialize the main window
window = tk.Tk()
window.geometry("700x700")
window.title("REGISTRATION FORM")
window.configure(background="grey")

# Define StringVars for entry fields
Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.StringVar()
var = tk.IntVar()
age = tk.StringVar()
password = tk.StringVar()
password1 = tk.StringVar()

value = random.randint(1, 1000)
print(value)

# Create the database and table if it doesn't exist
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS registration
               (Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT, Gender TEXT, age TEXT, password TEXT)""")
db.commit()

def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        ms.showinfo('Message', 'Password length should be at least 6')
        val = False
    if len(passwd) > 20:
        ms.showinfo('Message', 'Password length should not be greater than 20')
        val = False
    if not any(char.isdigit() for char in passwd):
        ms.showinfo('Message', 'Password should have at least one numeral')
        val = False
    if not any(char.isupper() for char in passwd):
        ms.showinfo('Message', 'Password should have at least one uppercase letter')
        val = False
    if not any(char.islower() for char in passwd):
        ms.showinfo('Message', 'Password should have at least one lowercase letter')
        val = False
    if not any(char in SpecialSym for char in passwd):
        ms.showinfo('Message', 'Password should have at least one of the symbols $@#')
        val = False
    return val

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = 'SELECT * FROM registration WHERE username = ?'
    c.execute(find_user, [(username.get())])

    # Validate email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    a = bool(re.search(regex, email))

    # Perform input validation
    if fname.isdigit() or fname == "":
        ms.showinfo("Message", "Please enter a valid name")
    elif addr == "":
        ms.showinfo("Message", "Please enter address")
    elif email == "" or not a:
        ms.showinfo("Message", "Please enter a valid email")
    elif len(mobile) != 10 or not mobile.isdigit():
        ms.showinfo("Message", "Please enter a 10-digit mobile number")
    elif not time.isdigit() or int(time) > 100 or int(time) == 0:
        ms.showinfo("Message", "Please enter a valid age")
    elif c.fetchall():
        ms.showerror('Error!', 'Username taken. Try a different one.')
    elif un == "" or len(un) != 10:
        ms.showinfo("Message", "Please enter a valid username")
    elif pwd == "":
        ms.showinfo("Message", "Please enter a valid password")
    elif gender not in [1, 2]:
        ms.showinfo("Message", "Please select gender")
    elif not password_check(pwd):
        pass  # password_check already shows the relevant message
    elif pwd != cnpwd:
        ms.showinfo("Message", "Password and Confirm Password must be the same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration (Fullname, address, username, Email, Phoneno, Gender, age, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (fname, addr, un, email, mobile, gender, time, pwd)
            )
            conn.commit()
            ms.showinfo('Success!', 'Account Created Successfully!')
            window.destroy()
            call(["python", "log.py"])

# For background image
image2 = Image.open('b2.jpg')
image2 = image2.resize((700, 700), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(window, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# UI Elements
l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 20, "bold", 'italic'), bg="red", fg="white")
l1.place(x=240, y=30)

l2 = tk.Label(window, text="Full Name:", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=130, y=100)
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=330, y=100)

l3 = tk.Label(window, text="Address:", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l3.place(x=130, y=150)
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=330, y=150)

l5 = tk.Label(window, text="E-mail:", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l5.place(x=130, y=200)
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=330, y=200)

l6 = tk.Label(window, text="Phone Number:", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l6.place(x=130, y=250)
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=330, y=250)

l7 = tk.Label(window, text="Gender:", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l7.place(x=130, y=300)
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=var, value=1).place(x=330, y=300)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=var, value=2).place(x=440, y=300)

l8 = tk.Label(window, text="Age:", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l8.place(x=130, y=350)
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=330, y=350)

l4 = tk.Label(window, text="User Name:", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l4.place(x=130, y=400)
t3 = tk.Entry(window, textvar=username, width=20, font=('', 15))
t3.place(x=330, y=400)

la = tk.Label(window, text="Note: Enter Mobile Number as a Username...!", width=40, font=("Times new roman", 10, "bold"), bg="black", fg="red")
la.place(x=300, y=450)

l9 = tk.Label(window, text="Password:", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l9.place(x=130, y=500)
t9 = tk.Entry(window, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=330, y=500)

l10 = tk.Label(window, text="Confirm Password:", width=15, font=("Times new roman", 15, "bold"), bg="snow")
l10.place(x=130, y=550)
t10 = tk.Entry(window, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=330, y=550)

btn = tk.Button(window, text="Register", bg="red", font=("", 20), fg="white", width=9, height=1, command=insert)
btn.place(x=260, y=620)

window.mainloop()