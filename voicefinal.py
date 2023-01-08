import speech_recognition as sr 
import os
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
root3=Tk()
root3.geometry("733x566")
root3.resizable(0,0)
root3.title("audio to text file")
text=StringVar()
bg=PhotoImage(file="F:/proj sem4/back1.png")
my_label=Label(root3,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

def cleartext():
    show_text.delete(1.0,END)
    file = open("F:\proj sem4\demo.txt","w")
    file.close()
def printit():
    text_file=open("F:\proj sem4\demo.txt",'r')
    print_text=text_file.read()
    show_text.insert(END,print_text)
    text_file.close()

def recog():
    global text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Now: ')
        showinfo("python says","Speak Now")
        audio = r.listen(source)
        print ('Recognition Done!')
        showinfo("python says"," Recognition Done! ")
        

    try:
        text=r.recognize_google(audio)
        Label(root3,textvariable='text',font="comicsansms 15 bold",fg="black").pack(pady="20",padx="20")
        #save_file(text)
    except Exception:
        print('Sorry...Run Again!')
def save_file():
    
    #Dialog Box to open Text File.
    savefile = filedialog.asksaveasfilename(initialdir='This PC', title = 'Save File', filetypes= (('Text Files','txt.*'), ('All Files','*.*')))
    #Open Saved File
    txtfile = open(savefile, 'a')
    txtfile1 = open("F:\proj sem4\demo.txt",'r+')
    #write in Saved File
    txtfile.writelines(text)
    txtfile1.writelines(text)
Label(root3,text="Audio To Text",font="comicsansms 30 bold",fg="red").pack()
Label(root3,text="Some info about ",font="comicsansms 15 bold",fg="black").pack(pady="20",padx="20")
bt6=Button(root3,text="Speak",command=recog)
bt6.pack(padx="200",pady="5",side="top",)
bt7=Button(root3,text="Save",command=save_file)
bt7.pack(padx="200",pady="5",side="top",)
show_text=Text(root3,width=50,height=10,font=("Helvetica", 16))
show_text.pack()
bt8=Button(root3,text="view text",command=printit)
bt8.pack(padx="200",pady="5",side="top",)
bt9=Button(root3,text="clear text",command=cleartext)
bt9.pack(padx="200",pady="5",side="top",)
bt10=Button(root3,text="Exit",command=exit)
bt10.pack(padx="200",pady="5",side="top",)


root3.mainloop()