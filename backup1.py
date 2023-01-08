import speech_recognition as sr 
import os
from tkinter import filedialog
from tkinter import *
from tkinter.messagebox import showinfo
root=Tk()
root.geometry("733x566")
root.title("Audio and Text Processing")
bg= PhotoImage(file="F:/proj sem4/back.png")
text=StringVar()

#audio to text page connected to the first open button

def attfpage():
    f2=Frame()
    f2.place(x="0",y="0",width="733",height="566")
    Label(f2, image=bg).place(x="0",y="0",relwidth="1",relheight="1")
    Label(f2,text="Audio To Text",font="comicsansms 30 bold",fg="red").grid()
    Label(f2,text="Some info about ",font="comicsansms 10 bold",fg="black").grid(pady="10",padx="20")

    def cleartext():
        show_text.delete(1.0,END)
        txtfile1= open("demo.txt",'w')
        txtfile1.close()
    def printit():
        text_file=open("demo.txt",'r')
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
            Label(f2,textvariable='text',font="comicsansms 10 bold",fg="black").grid(pady="10",padx="20")
            #save_file(text)
        except Exception:
            print('Sorry...Run Again!')
    def save_file():
        
        #Dialog Box to open Text File.
        savefile = filedialog.asksaveasfilename(initialdir='This PC', title = 'Save File', filetypes= (('Text Files','txt.*'), ('All Files','*.*')))
        #Open Saved File
        txtfile = open(savefile, 'a')
        txtfile1= open("demo.txt",'r+')
        #write in Saved File
        txtfile.writelines(text)
        txtfile1.writelines(text)
    
    bt21=Button(f2,text="Speak",command=recog)
    bt21.grid(padx="200",pady="5")
    bt22=Button(f2,text="Save",command=save_file)
    bt22.grid(padx="200",pady="5")
    show_text=Text(f2,width=50,height=10,font=("Helvetica", 16))
    show_text.grid(padx="65",pady="5")
    bt23=Button(f2,text="view text",command=printit)
    bt23.grid(padx="200",pady="5")
    bt24=Button(f2,text="clear text",command=cleartext)
    bt24.grid(padx="200",pady="5")
    bt25=Button(f2,text="Exit",command=exit)
    bt25.grid(padx="200",pady="5")    

    bt26=Button(f2,text="Go Back",command=mainpage)
    bt26.grid(pady="5")
    bt27=Button(f2,text="Exit",command=exit)
    bt27.grid(pady="5",padx="35")

#first page of app with three options

def mainpage():
    f0=Frame()
    f0.place(x="0",y="0",width="733",height="566")
    Label(f0, image=bg).place(x="0",y="0",relwidth="1",relheight="1")
    Label(f0,text="Text And Audio Processing",font="comicsansms 30 bold",fg="red").grid(row=0,column=0)
    Label(f0,text=" GUI Application",font="comicsansms 30 bold",fg="red").grid(row=1,column=0)
    f1= Frame(f0,width="733")
    f1.grid(padx="70",pady="5")
    
    l1=Label(f1,text="Audio To Text",font="Times 20 bold")
    l1.grid(row=2,column=0)
    l2=Label(f1,text="     Audio To Text lets you process audio files or voices to text files",font="Times 10 bold")
    l2.grid(row=3,column=0)
    bt1=Button(f1,text="Open",command=attfpage,font=("comicsansms","10"))
    bt1.grid(row=4,column=0,pady="5")
    bt188=Button(f1,text="Open",font=("comicsansms","10"))
    bt188.grid(row=5,column=0,pady="5")
    

    l3=Label(f1,text="Text To Audio",font="Times 20 bold")
    l3.grid(row=6,column=0,padx="35")
    l4=Label(f1,text="Text To Audio lets you process Text files to Audio files",font="Times 10 bold")
    l4.grid(row=7,column=0,padx="35")
    bt01=Button(f1,text="Open",command="",font=("comicsansms","10"))
    bt01.grid(row=8,column=0,pady="5",padx="35")

    l5=Label(f1,text="Language Translator",font="Times 20 bold")
    l5.grid(row=9,column=0,padx="35")
    l6=Label(f1,text="Translate one language to another",font="Times 10 bold")
    l6.grid(row=10,column=0,padx="35")
    bt2=Button(f1,text="Open",command="",font=("comicsansms","10"))
    bt2.grid(row=11,column=0,pady="5",padx="35")
    bt00=Button(f1,text="Exit",command=exit,font=("comicsansms","10"))
    bt00.grid(row=12,column=0,pady="5",padx="35")

mainpage()
root.mainloop()