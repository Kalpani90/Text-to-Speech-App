import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
#from PIL import Image, ImageTk


root = Tk()
root.title("Converting Text to Speech")
root.geometry('950x470+200+200')
root.resizable(False,False)
root.configure(bg="#305065")

engine = pyttsx3.init()

#Defining a function for speak and speed
def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices= engine.getProperty('voices')

    def setvoice():

        if gender == "Male":
            engine.setProperty('voice', voices[4].id)
            engine.say(text)
            engine.runAndWait()

        else:
            engine.setProperty('voice', 'english_rp+f3')
            engine.say(text)
            engine.runAndWait()


    if text:
        if (speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()

        elif(speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()

        else:
            engine.setProperty('rate',60)
            setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():

        if gender == "Male":
            engine.setProperty('voice', voices[4].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

        else:
            engine.setProperty('voice', 'english_rp+f3')
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()


    if text:
        if (speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()

        elif(speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()

        else:
            engine.setProperty('rate',60)
            setvoice()




#Displaying the icon
image_icon = PhotoImage(file="text_to_speech/download.png")
#image_icon = Image.open("download.png")
root.iconphoto(False,image_icon)
root.wm_title("Text to Speech App")


#Top Frame
Top_frame= Frame(root,bg="white", width= 950, height= 120)
Top_frame.place(x=0, y=0)
Logo = PhotoImage(file="text_to_speech/imagesr.png")
img_logo = Logo.subsample(2)
Label(Top_frame,image=img_logo ,bg="white").place(x=10,y=5)
Label(Top_frame,text="TEXT TO SPEECH", font="Helvetica 20 bold", bg="white",fg="black").place(x=100, y= 30)

#Text Area
text_area = Text(root,font="Robote 20",bg="white",relief=GROOVE, wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

#Label for Voice and Speed
Label(root,text="VOICE",font="arial 15 bold", bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold", bg="#305065",fg="white").place(x=760,y=160)

#Combo Box for gender 
gender_combobox = Combobox(root,values=['Male','Female'],font="Helvetica 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

#Combo Box for speed
speed_combobox = Combobox(root,values=['Fast','Normal','Slow'],font="Helvetica 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

#Speak Button
image_ic = PhotoImage(file="text_to_speech/speak.png")
img_speak = image_ic.subsample(6)
btn = Button(root,text="Speak",compound=LEFT,image=img_speak,width=130,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)

#Download Button
image_download = PhotoImage(file="text_to_speech/downloadh.png")
img_load = image_download.subsample(4)
download_image= Button(root,text="Download",compound=LEFT,image=img_load,width=130,font="arial 14 bold", command=download)
download_image.place(x=730,y=280)



root.mainloop()