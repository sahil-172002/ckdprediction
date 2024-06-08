
import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("CKD Prediction using Machine Learning")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('crop5.jpg')
# image2 = image2.resize((w,h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



#
label_l1 = tk.Label(root, text="Chronic Kidney Disease Detection",font=("Times New Roman", 30, 'bold'),
                    background="#006400", fg="white", width=67, height=2)
label_l1.place(x=0, y=0)

img = Image.open('b1.jpg')
img = img.resize((100,70), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=40, y=10)


img=ImageTk.PhotoImage(Image.open("b7.jpg"))

img2=ImageTk.PhotoImage(Image.open("b8.jpg"))

img3=ImageTk.PhotoImage(Image.open("b9.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=95)


logo_label1=tk.Label(text='"Early detection of CKD allows proper management \n that could slow down CKD progression, prevent cardiovascular \n and other comorbidities and enable timely initiation of dialysis."',compound='bottom',font=("Times New Roman", 20, 'bold', 'italic'),width=65, bg="black", fg="white")
#logo_label=tk.Label(height=500, width=400)
logo_label1.place(x=300,y=600)



# using recursion to slide to next image
x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img,width=1800,height=700)
	elif x == 2:
		logo_label.config(image=img2,width=1800,height=700)
	elif x == 3:
		logo_label.config(image=img3,width=1800,height=700)
	x = x+1
	root.after(2000, move)

# calling the function
move()

frame_alpr = tk.LabelFrame(root, text=" --Login & Register-- ", width=1800, height=100, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=0, y=100)


#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    
def reg():
    from subprocess import call
    call(["python","registration.py"])
    #root.destroy()
def log():
    from subprocess import call
    call(["python","log.py"])
    #root.destroy()
def window():
  root.destroy()
  
  


#####################################################################################################################

button1 = tk.Button(frame_alpr, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="Black", fg="white")
button1.place(x=300, y=10)
button2 = tk.Button(frame_alpr, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
button2.place(x=700, y=10)

button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
button3.place(x=1100, y=10)


label_l1 = tk.Label(root, text="** Crop Predication System **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=250, height=2)
label_l1.place(x=0, y=800)


root.mainloop()