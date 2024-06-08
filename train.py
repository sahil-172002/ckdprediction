import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from subprocess import Popen

root = tk.Tk()
root.title("train")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

image2 = Image.open('b1.jpg')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

label_l2 = tk.Label(root, text="___CKD Disease Detection System___", font=("times", 30, 'bold', 'italic'),
                    background="green", fg="white", width=70, height=2)
label_l2.place(x=0, y=0)

data = pd.read_csv("kidney_disease.csv")
data = data.dropna()
le = LabelEncoder()

def Data_Preprocessing():
    data = pd.read_csv("kidney_disease.csv")
    data = data.dropna()

    le = LabelEncoder()
    data['id'] = le.fit_transform(data['id'])
    data['age'] = le.fit_transform(data['age'])
    data['bp'] = le.fit_transform(data['bp'])
    data['sg'] = le.fit_transform(data['sg'])
    data['al'] = le.fit_transform(data['al'])
    data['su'] = le.fit_transform(data['su'])
    data['rbc'] = le.fit_transform(data['rbc'])
    data['pc'] = le.fit_transform(data['pc'])
    data['pcc'] = le.fit_transform(data['pcc'])
    data['ba'] = le.fit_transform(data['ba'])
    data['bgr'] = le.fit_transform(data['bgr'])
    data['bu'] = le.fit_transform(data['bu'])
    data['sc'] = le.fit_transform(data['sc'])
    data['sod'] = le.fit_transform(data['sod'])
    data['pot'] = le.fit_transform(data['pot'])
    data['hemo'] = le.fit_transform(data['hemo'])
    data['pcv'] = le.fit_transform(data['pcv'])
    data['wc'] = le.fit_transform(data['wc'])
    data['rc'] = le.fit_transform(data['rc'])
    data['htn'] = le.fit_transform(data['htn'])
    data['dm'] = le.fit_transform(data['dm'])
    data['cad'] = le.fit_transform(data['cad'])
    data['appet'] = le.fit_transform(data['appet'])
    data['pe'] = le.fit_transform(data['pe'])
    data['ane'] = le.fit_transform(data['ane'])

    x = data.drop(['classification'], axis=1)
    y = data['classification']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="grey",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=200, y=120)

def Model_Training():
    data = pd.read_csv("kidney_disease.csv")
    data = data.dropna()

    le = LabelEncoder()
    data['id'] = le.fit_transform(data['id'])
    data['age'] = le.fit_transform(data['age'])
    data['bp'] = le.fit_transform(data['bp'])
    data['sg'] = le.fit_transform(data['sg'])
    data['al'] = le.fit_transform(data['al'])
    data['su'] = le.fit_transform(data['su'])
    data['rbc'] = le.fit_transform(data['rbc'])
    data['pc'] = le.fit_transform(data['pc'])
    data['pcc'] = le.fit_transform(data['pcc'])
    data['ba'] = le.fit_transform(data['ba'])
    data['bgr'] = le.fit_transform(data['bgr'])
    data['bu'] = le.fit_transform(data['bu'])
    data['sc'] = le.fit_transform(data['sc'])
    data['sod'] = le.fit_transform(data['sod'])
    data['pot'] = le.fit_transform(data['pot'])
    data['hemo'] = le.fit_transform(data['hemo'])
    data['pcv'] = le.fit_transform(data['pcv'])
    data['wc'] = le.fit_transform(data['wc'])
    data['rc'] = le.fit_transform(data['rc'])
    data['htn'] = le.fit_transform(data['htn'])
    data['dm'] = le.fit_transform(data['dm'])
    data['cad'] = le.fit_transform(data['cad'])
    data['appet'] = le.fit_transform(data['appet'])
    data['pe'] = le.fit_transform(data['pe'])
    data['ane'] = le.fit_transform(data['ane'])

    x = data.drop(['classification'], axis=1)
    y = data['classification']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=6)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear', random_state=6)
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    repo = classification_report(y_test, y_pred)

    label4 = tk.Label(root, text=str(repo), width=45, height=10, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=205, y=200)

    label5 = tk.Label(root, text="Accuracy : " + str(accuracy * 100) + "%\nModel saved as SVM_CKD_MODEL.joblib", width=45, height=3, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label5.place(x=205, y=420)

    from joblib import dump
    dump(svcclassifier, "SVM_CKD_MODEL.joblib")
    print("Model saved as SVM_CKD_MODEL.joblib")

def predication():
    Popen(["python", "predication.py"])
    root.destroy()

def window():
    root.destroy()

button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
button2.place(x=5, y=120)

button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=5, y=220)

button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="CKD prediction", command=predication, width=15, height=2)
button4.place(x=5, y=320)

exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, 'bold'), bg="red", fg="white")
exit.place(x=5, y=450)

root.mainloop()