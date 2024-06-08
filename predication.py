from tkinter import *
import tkinter as ttk

def Train():
    """GUI"""
    import tkinter as tk
    

    import numpy as np
    import pandas as pd
    from PIL import Image, ImageTk

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    #root.geometry("800x850+0+0")
    root.title("Detect Disease")
    root.configure(background="purple")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    image2 = Image.open('b1.jpg')

    image2 = image2.resize((w, h), Image.LANCZOS)
    
    background_image = ImageTk.PhotoImage(image2)
    
    
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

    
    #StationId = tk.StringVar()
    id = tk.IntVar()
    age = tk.IntVar()
    bp = tk.IntVar()
    sg = tk.DoubleVar()
    al = tk.IntVar()
    su = tk.IntVar()
    rbc= tk.IntVar()
    pc = tk.IntVar()
    pcc = tk.IntVar()
    ba = tk.IntVar()
    bgr = tk.IntVar()
    bu = tk.IntVar()
    sc = tk.DoubleVar()
    sod = tk.IntVar()
    pot = tk.DoubleVar()
    hemo = tk.DoubleVar()
    pcv = tk.IntVar()
    wc = tk.IntVar()
    rc = tk.DoubleVar()
    htn = tk.IntVar()
    dm = tk.IntVar()
    cad = tk.IntVar()
    appet = tk.IntVar()
    pe = tk.IntVar()
    ane = tk.IntVar()
    #===============================================================================================



    def Detect():
        e1=id.get()
        print(e1)
        
        e2=age.get()
        print(e2)
        
        e3=bp.get()
        print(e3)
        e4=sg.get()
        print(e4)
        e5=al.get()
        print(e5)
        e6=su.get()
        print(e6)
        e7=rbc.get()
        print(e7)
        e8=pc.get()
        print(e8)
        e9=pcc.get()
        print(e9)
        e10=ba.get()
        print(e10)
        e11=bgr.get()
        print(e11)
        e12=bu.get()
        print(e12)
        e13=sc.get()
        print(e13)
        e14=sod.get()
        print(e14)
        e15=pot.get()
        print(e15)
        e16=hemo.get()
        print(e16)
        e17=pcv.get()
        print(e17)
        e18=wc.get()
        print(e18)
        e19=rc.get()
        print(e19)
        e20=htn.get()
        print(e20)
        e21=dm.get()
        print(e21)
        e22=cad.get()
        print(e22)
        e23=appet.get()
        print(e23)
        e24=pe.get()
        print(e24)
        e25=ane.get()
        print(e25)
       
        #########################################################################################
        
        from joblib import dump , load
        a1 = load('SVM_CKD_MODEL.joblib')
        v= a1.predict([[e1,e2, e3, e4, e5, e6, e7, e8, e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]])
        print(v)
        if v[0]=="ckd":
            print("Chronic Kidney Disease Detected")
            l1 = tk.Label(frame_alpr,text="Chronic Kidney \nDisease Detected",background="Green",foreground="white",font=('times', 20, ' bold '),width=15)
            l1.place(x=700,y=300)   
            
        elif v[0]=="notckd":
            print("Chrnoic Kidney Disease Not Detected")
            lab1 = tk.Label(frame_alpr, text="Chrnoic Kidney Disease \nNot Detected", background="Red", foreground="white",font=('times', 20, ' bold '),width=15)
            lab1.place(x=700, y=300)
       

    
    frame_alpr = tk.LabelFrame(root, text=" --Disease Detection-- ", width=1000, height=800, bd=5, font=('Algerian', 14, ' bold '),bg="white")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=0, y=0)


    l2=tk.Label(frame_alpr,text="id",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l2.place(x=20,y=20)
    sex=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=id)
    sex.place(x=200,y=20)

    l3=tk.Label(frame_alpr,text="age",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l3.place(x=20,y=60)
    chest_pain=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=age)
    chest_pain.place(x=200,y=60)
    
   
    l4=tk.Label(frame_alpr,text="bp",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l4.place(x=20,y=100)
    restbp=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=bp)
    restbp.place(x=200,y=100)

    l5=tk.Label(frame_alpr,text="sg",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l5.place(x=20,y=140)
    chol=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sg)
    chol.place(x=200,y=140)

    l6=tk.Label(frame_alpr,text="al",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l6.place(x=20,y=180)
    fbs=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=al)
    fbs.place(x=200,y=180)

    l7=tk.Label(frame_alpr,text="su",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l7.place(x=20,y=220)
    restecg=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=su)
    restecg.place(x=200,y=220)

    l8 = tk.Label(frame_alpr, text="rbc:",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l8.place(x=20, y=260)
   # gender
    tk.Radiobutton(frame_alpr, text="normal", padx=5, width=5, bg="snow", font=("bold", 15), variable=rbc, value=1).place(x=200,
                                                                                                                y=260)
    tk.Radiobutton(frame_alpr, text="abnormal", padx=20, width=4, bg="snow", font=("bold", 15), variable=rbc, value=2).place(
    x=200, y=290)
    
    l9 = tk.Label(frame_alpr, text="pc:", background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l9.place(x=20, y=330)
   # gender
    tk.Radiobutton(frame_alpr, text="normal", padx=5, width=5, bg="snow", font=("bold", 15), variable=pc, value=1).place(x=200,
                                                                                                                y=330)
    tk.Radiobutton(frame_alpr, text="abnormal", padx=20, width=4, bg="snow", font=("bold", 15), variable=pc, value=2).place(
    x=200, y=360)

    l10 = tk.Label(frame_alpr, text="pcc:",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l10.place(x=20, y=400)
   # gender
    tk.Radiobutton(frame_alpr, text="present", padx=5, width=5, bg="snow", font=("bold", 15), variable=pcc, value=1).place(x=200,
                                                                                                                y=400)
    tk.Radiobutton(frame_alpr, text="not present", padx=20, width=6, bg="snow", font=("bold", 15), variable=pcc, value=2).place(
    x=200, y=430)

    l11= tk.Label(frame_alpr, text="ba:", background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l11.place(x=20, y=470)
# gender
    tk.Radiobutton(frame_alpr, text="present", padx=5, width=5, bg="snow", font=("bold", 15), variable=ba, value=1).place(x=200,
                                                                                                             y=470)
    tk.Radiobutton(frame_alpr, text="not present", padx=20, width=6, bg="snow", font=("bold", 15), variable=ba, value=2).place(
    x=200, y=500)
 
    l12=tk.Label(frame_alpr,text="bgr",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l12.place(x=20,y=540)
    exang=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=bgr)
    exang.place(x=200,y=540)

    l13=tk.Label(frame_alpr,text="bu",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l13.place(x=20,y=580)
    oldpeak=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=bu)
    oldpeak.place(x=200,y=580)

    l14=tk.Label(frame_alpr,text="sc",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l14.place(x=400,y=20)
    oldpeak=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sc)
    oldpeak.place(x=580,y=20)
    
    l14=tk.Label(frame_alpr,text="sod",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l14.place(x=400,y=60)
    oldpeak=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sod)
    oldpeak.place(x=580,y=60)
    
    l15=tk.Label(frame_alpr,text="pot",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l15.place(x=400,y=100)
    oldpeak=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=pot)
    oldpeak.place(x=580,y=100)
    
    l16=tk.Label(frame_alpr,text="hemo",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l16.place(x=400,y=140)
    oldpeak=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=hemo)
    oldpeak.place(x=580,y=140)
    
    l17=tk.Label(frame_alpr,text="pcv",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l17.place(x=400,y=180)
    oldpeak=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=pcv)
    oldpeak.place(x=580,y=180)
    
    l18=tk.Label(frame_alpr,text="wc",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l18.place(x=400,y=220)
    oldpeak=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=wc)
    oldpeak.place(x=580,y=220)
    
    l19=tk.Label(frame_alpr,text="rc",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l19.place(x=400,y=260)
    oldpeak=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=rc)
    oldpeak.place(x=580,y=260)
    
    l20 = tk.Label(frame_alpr, text="htn:", background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l20.place(x=400, y=300)
# gender
    tk.Radiobutton(frame_alpr, text="yes", padx=5, width=5, bg="snow", font=("bold", 15), variable=htn, value=1).place(x=580,
                                                                                                             y=300)
    tk.Radiobutton(frame_alpr, text="no", padx=20, width=2, bg="snow", font=("bold", 15), variable=htn, value=2).place(
    x=580, y=330)
    
# gender

    l21 = tk.Label(frame_alpr, text="dm:", background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l21.place(x=400, y=370)
# gender
    tk.Radiobutton(frame_alpr, text="yes", padx=5, width=5, bg="snow", font=("bold", 15), variable=dm, value=1).place(x=580,
                                                                                                             y=370)
    tk.Radiobutton(frame_alpr, text="no", padx=20, width=2, bg="snow", font=("bold", 15), variable=dm, value=2).place(
    x=580, y=400)

    
    l22 = tk.Label(frame_alpr, text="cad:", background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l22.place(x=400, y=440)
# gender
    tk.Radiobutton(frame_alpr, text="yes", padx=5, width=5, bg="snow", font=("bold", 15), variable=cad, value=1).place(x=580,
                                                                                                             y=440)
    tk.Radiobutton(frame_alpr, text="no", padx=20, width=2, bg="snow", font=("bold", 15), variable=cad, value=2).place(
    x=580, y=470)
   
    l23 = tk.Label(frame_alpr, text="appet:", background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l23.place(x=400, y=510)
 # gender
    tk.Radiobutton(frame_alpr, text="good", padx=5, width=5, bg="snow", font=("bold", 15), variable=appet, value=1).place(x=580,
                                                                                                              y=510)
    tk.Radiobutton(frame_alpr, text="poor", padx=20, width=2, bg="snow", font=("bold", 15), variable=appet, value=2).place(
     x=580, y=540)
   
    
    l24 = tk.Label(frame_alpr, text="pe:",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l24.place(x=700, y=20)
# gender
    tk.Radiobutton(frame_alpr, text="yes", padx=5, width=5, bg="snow", font=("bold", 15), variable=pe, value=1).place(x=880,
                                                                                                             y=20)
    tk.Radiobutton(frame_alpr, text="no", padx=20, width=2, bg="snow", font=("bold", 15), variable=pe, value=2).place(
    x=880, y=50)

    l25= tk.Label(frame_alpr, text="ane:",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l25.place(x=700, y=90)
# gender
    tk.Radiobutton(frame_alpr, text="yes", padx=5, width=5, bg="snow", font=("bold", 15), variable=ane, value=1).place(x=880,
                                                                                                             y=90)
    tk.Radiobutton(frame_alpr, text="no", padx=20, width=2, bg="snow", font=("bold", 15), variable=ane, value=2).place(
    x=880, y=120)
 
    button1 = tk.Button(frame_alpr,text="Submit",command=Detect,font=('times', 20, ' bold '),background='brown',width=10)
    button1.place(x=700,y=200)


    root.mainloop()
Train()
