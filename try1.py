from tkinter import *
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
import pyttsx3
 
# root window
root = Tk()
root.resizable(0,0)
root.geometry("533x566")
#root.configure(background="white")
bg=PhotoImage(file="F:/proj sem4/back.png")
my_label=Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)
root.title("Text To Speak")
Label(root,text="",font="comicsansms 13 bold").grid(row=1,column=5)
volm= Label(root,text="Reading speed(20-250)")
volm.grid(row=1,column=4)
namevalue=StringVar()
nameentry=Entry(root,textvariable=namevalue)
nameentry.grid(row=2,column=4)
v=IntVar()



# functions

def getvals():
    global v
    v=namevalue.get()
    print(f"{namevalue.get()}")

def speak():
    print(v)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    audio_string = text.get(1.0,END)
    engine.setProperty('rate',int(v))
    engine.say(audio_string)
    engine.runAndWait()
    engine.stop()
 
 
def save_audio():
    engine = pyttsx3.init()
    audio_string = text.get(1.0,END)
    engine.save_to_file(audio_string,'test.mp3')
    engine.runAndWait()
    engine.stop()
    showinfo("python says","audio is saved as text.mp3")
 
# root widgets
text = scrolledtext.ScrolledText(root,width=40,height=10,wrap=WORD,padx=10,pady=10,borderwidth=5,relief=RIDGE)
text.grid(row=0,columnspan=5)

#buttons
bt1=Button(root,text="Listen",width=7,command=speak)
bt1.grid(row=2,column=0,ipadx=2)
bt2=Button(root,text="Change",width=7,command=getvals)
bt2.grid(row=3,column=4,ipadx=2)
bt3=Button(root,text="Clear",width=7,command=lambda:text.delete(1.0,END))
bt3.grid(row=2,column=1,ipadx=2)
bt4=Button(root,text="Save",width=7,command=save_audio)
bt4.grid(row=2,column=2,ipadx=2)
bt5=Button(root,text="Exit",width=7,command=root.quit)
bt5.grid(row=2,column=3,ipadx=2)
root.mainloop()