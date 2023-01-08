from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
import os
from gtts import gTTS
from playsound import playsound
from tkinter import Tk
from tkinter.filedialog import askopenfilename
 
# root window
root=Tk()
root.geometry("280x125")
Tk().withdraw()
#filelocation = askopenfilename()
root.resizable(0,0)
#root.configure(background="white")
bg=PhotoImage(file="F:/proj sem4/back2.png")
my_label=Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)


root.title("TextFile To Audio")
#f=open(filelocation, "rt")
#x=f.read()
                  
#language = input("Language Name--> ")

name=Label(root,text="   Language-->")
name.grid(row=1,column=6)
namevalue=StringVar()
nameentry=Entry(root,textvariable=namevalue)
nameentry.grid(row=1,column=7,ipadx=2)
var=StringVar()
var='en'





# functions

def getvals():
    print("Language changed to ")
    print(f"{namevalue.get()}")
    global var
    var=namevalue.get()
    #print(var)



def speak():
    #print(var)
    f=open(filelocation, "rt")
    x=f.read()
    myobj = gTTS(text=x, lang=var , slow=False)
    playsound("hi.mp3")
 
 
def save_audio():
    #print(var)
    global myobj
    f=open(filelocation, "rt")
    x=f.read()
    myobj = gTTS(text=x, lang=var, slow=False)
    myobj.save("hi.mp3")
    f.close()  
    showinfo("python says","audio is saved as text.mp3")

def selectf():
    
    #Tk().withdraw()
    global filelocation
    filelocation = askopenfilename()
    f=open(filelocation, "rt")
    x=f.read()
    


bt43=Button(root,text="Listen",width=12,command=speak)
bt43.grid(row=4,column=1,ipadx=2)
bt44=Button(root,text="Change",width=12,command=getvals)
bt44.grid(row=2,column=7,ipadx=2)
bt45=Button(root,text="Select File",width=12,command=selectf)
bt45.grid(row=1,column=1,ipadx=2)
bt46=Button(root,text="Save",width=12,command=save_audio)
bt46.grid(row=3,column=1,ipadx=2)
bt47=Button(root,text="Exit",width=12,command=root.quit)
bt47.grid(row=5,column=1,ipadx=2)

root.mainloop()
