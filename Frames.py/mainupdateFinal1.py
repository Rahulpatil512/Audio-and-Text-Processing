import speech_recognition as sr
import os
from tkinter import filedialog
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
import tkinter.scrolledtext as scrolledtext
import pyttsx3
from gtts import gTTS
from playsound import playsound
from tkinter import Tk
f3 = Tk()
f3.geometry("533x566")
f3.title("Audio and Text Processing")
bg = PhotoImage(file="F:/proj sem4/back1.png")
text = StringVar()
v = IntVar()
var = StringVar()
var = 'en'
namevalue = StringVar()
# audio to text page connected to the first open button(speak version)


def attfpage():
    f2 = Frame()
    f2.place(x="0", y="0", width="533", height="566")
    Label(f2, image=bg).place(x="0", y="0", relwidth="1", relheight="1")
    Label(f2, text="Audio To Text", font="comicsansms 30 bold",
          fg="lightblue").grid(padx=134)
    #Label(f2,text="Some info about ",font="comicsansms 10 bold",fg="black").grid(pady="10",padx="20")

    def cleartext():
        show_text.delete(1.0, END)
        txtfile1 = open("demo.txt", 'w')
        txtfile1.close()

    def printit():
        text_file = open("demo.txt", 'r')
        print_text = text_file.read()
        show_text.insert(END, print_text)
        text_file.close()

    def recog():
        global text
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Speak Now: ')
            showinfo("python says", "Speak Now")
            audio = r.listen(source)
            print('Recognition Done!')
            showinfo("python says", " Recognition Done! ")

        try:
            text = r.recognize_google(audio)
            Label(f2, textvariable='text', font="comicsansms 10 bold",
                  fg="black").grid(pady="10", padx="20")
            # save_file(text)
        except Exception:
            print('Sorry...Run Again!')

    def save_file():

        # Dialog Box to open Text File.
        savefile = filedialog.asksaveasfilename(initialdir='This PC', title='Save File', filetypes=(
            ('Text Files', 'txt.*'), ('All Files', '*.*')))
        # Open Saved File
        txtfile = open(savefile, 'a')
        txtfile1 = open("demo.txt", 'r+')
        # write in Saved File
        txtfile.writelines(text)
        txtfile1.writelines(text)

    bt21 = Button(f2, text="Speak", command=recog)
    bt21.grid(pady="5",)
    bt22 = Button(f2, text="Save", command=save_file)
    bt22.grid(pady="5",)
    show_text = Text(f2, width=43, height=10, font=("Helvetica", 16))
    show_text.grid()
    bt23 = Button(f2, text="view text", command=printit)
    bt23.grid(pady="5",)
    bt24 = Button(f2, text="clear text", command=cleartext)
    bt24.grid(pady="5",)

    bt26 = Button(f2, text="Go Back", command=mainpage)
    bt26.grid(pady="5")
    bt27 = Button(f2, text="Exit", command=exit)
    bt27.grid(pady="5",)

# audio to text with file(file version)


def attf1():
    f10 = Frame()
    f10.place(x="0", y="0", width="533", height="566")
    Tk().withdraw()
    global filename
    #bg=PhotoImage(file="D:\Final MP 4\back1.png")
    my_label = Label(f10, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    def cleartext1():
        show_text.delete(1.0, END)
        file = open("demo.txt", "w")
        file.close()

    def printit1():
        text_file = open("demo.txt", 'r')
        print_text = text_file.read()
        show_text.insert(END, print_text)
        text_file.close()

    def selectf():

        # Tk().withdraw()
        global filelocation
        filelocation = askopenfilename()
        f = open(filelocation, "rt")
        global text
        # Tk().withdraw()
        #filelocation = askopenfilename()
        r = sr.Recognizer()
        with sr.AudioFile(filelocation) as source:
            audio = r.listen(source)
        print('File Recognizing...')
        showinfo("python says", " File Recognizing......\n Please Wait!!")
        try:
            text = r.recognize_google(audio)
            print('Recognition Done!')
            showinfo("python says", " Recognition Done! ")
        except:
            print('You Have Selected Wrong File!')
            showinfo("python says", " You Have Selected Wrong File! ")

    def save_file1():

        # Dialog Box to open Text File.
        savefile = filedialog.asksaveasfilename(initialdir='This PC', title='Save File', filetypes=(
            ('Text Files', 'txt.*'), ('All Files', '*.*')))
        # Open Saved File
        txtfile = open(savefile, 'a')
        txtfile1 = open("demo.txt", 'r+')
        # write in Saved File
        txtfile.writelines(text)
        txtfile1.writelines(text)

    Label(f10, text="Audio File To Text",
          font="comicsansms 30 bold", fg="lightblue").grid()
    #Label(f10,text="Some info about ",font="comicsansms 15 bold",fg="black").grid(pady="",padx="20")
    bt101 = Button(f10, text="Select File", command=selectf)
    bt101.grid(padx="200", pady="5")
    bt102 = Button(f10, text="Save", command=save_file1)
    bt102.grid(padx="200", pady="5")
    show_text = Text(f10, width=43, height=10, font=("Helvetica", 16))
    show_text.grid(padx=6)
    bt103 = Button(f10, text="view text", command=printit1)
    bt103.grid(padx="200", pady="5")
    bt104 = Button(f10, text="clear text", command=cleartext1)
    bt104.grid(padx="200", pady="5")
    bt106 = Button(f10, text="Go Back", command=mainpage)
    bt106.grid(pady="5")
    bt105 = Button(f10, text="Exit", command=exit)
    bt105.grid(padx="200", pady="5")


# Text to audio(Typing version)
def ttaf():
    f3 = Frame()
    namevalue = StringVar()
    # f3.resizable(0,0)
    f3.place(x="0", y="0", width="533", height="566")
    Label(f3, image=bg).place(x="0", y="0", relwidth="1", relheight="1")
    Label(f3, text="Text to Audio", font="comicsansms 30 bold",
          fg="lightblue").grid(padx=135)

    # functions

    def getvals():
        global v
        v = namevalue.get()
        print(f"{namevalue.get()}")

    def speak():
        print(v)
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        audio_string = text.get(1.0, END)
        engine.setProperty('rate', int(v))
        engine.say(audio_string)
        engine.runAndWait()
        engine.stop()

    def save_audio():
        engine = pyttsx3.init()
        audio_string = ""
        audio_string = text.get(1.0, END)
        a = len(audio_string)
        print(a)
        print(audio_string)
        if(a != 1): 
            engine.save_to_file(audio_string, 'test.mp3')
            engine.runAndWait()
            engine.stop()
            showinfo("python says", "audio is saved as text.mp3")
        else:
            showinfo("python says", "Please Input Text!!")


    # f3 widgets
    text = scrolledtext.ScrolledText(
        f3, width=50, height=10, wrap=WORD, padx=10, pady=10, borderwidth=5, relief=RIDGE)
    text.grid()

    # buttons
    volm = Label(f3, text="Reading speed(20-250)")
    volm.grid(pady=3)
    nameentry = Entry(f3, textvariable=namevalue)
    nameentry.grid()
    bt2 = Button(f3, text="Change", width=7, command=getvals)
    bt2.grid(ipadx=2, pady=5)
    bt1 = Button(f3, text="Listen", width=7, command=speak)
    bt1.grid(ipadx=2, pady=10)
    bt3 = Button(f3, text="Clear", width=7,
                 command=lambda: text.delete(1.0, END))
    bt3.grid(ipadx=2, pady=10)
    bt4 = Button(f3, text="Save", width=7, command=save_audio)
    bt4.grid(ipadx=2, pady=10)
    bt6 = Button(f3, text="Go Back", width=7, command=mainpage)
    bt6.grid(ipadx=2, pady=10)
    bt5 = Button(f3, text="Exit", width=7, command=exit)
    bt5.grid(ipadx=2, pady=10)


# Text file to audio (File version)

def ttaf1():
    f4 = Frame()
    f4.place(x="0", y="0", width="700", height="566")
    Label(f4, image=bg).place(x="0", y="0", relwidth="1", relheight="1")
    lb4 = Label(f4, text="Text File to Audio",
                font="comicsansms 30 bold", fg="lightblue")
    lb4.grid(padx="95")
    Tk().withdraw()
    name = Label(f4, text="   Language-->")
    name.grid()
    nameentry = Entry(f4, textvariable=namevalue)
    nameentry.grid()

# functions

    def getvals1():
        print("Language changed to ")
        print(f"{namevalue.get()}")
        global var
        var = namevalue.get()
        # print(var)

    def speak1():
        # print(var)
        f = open(filelocation, "rt")
        x = f.read()
        myobj = gTTS(text=x, lang=var, slow=False, tld='com')
        playsound("text.mp3")

    def save_audio1():
        # print(var)
        global myobj
        f = open(filelocation, "rt")
        x = f.read()
        myobj = gTTS(text=x, lang=var, slow=False, tld='com')
        myobj.save("text.mp3")
        f.close()
        showinfo("python says", "audio is saved as text.mp3")

    def selectf1():

        # Tk().withdraw()
        global filelocation
        filelocation = askopenfilename()
        global x
        try:
            f=open(filelocation, "rt")
            x=f.read()
        except:
            showinfo("Python says", "Please select .txt file!!")    

    bt44 = Button(f4, text="Change", width=12, command=getvals1)
    bt44.grid(ipadx=2, pady=10)
    bt45 = Button(f4, text="Select File", width=12, command=selectf1)
    bt45.grid(ipadx=2, pady=10)
    bt46 = Button(f4, text="Save", width=12, command=save_audio1)
    bt46.grid(ipadx=2, pady=10)
    bt43 = Button(f4, text="Listen", width=12, command=speak1)
    bt43.grid(ipadx=2, pady=10)
    bt47 = Button(f4, text="Go Back", width=12, command=mainpage)
    bt47.grid(ipadx=2, pady=10)
    bt47 = Button(f4, text="Exit", width=12, command=exit)
    bt47.grid(ipadx=2, pady=10)


# first page of app with three options

def mainpage():
    f0 = Frame()
    f0.place(x="0", y="0", width="533", height="566")
    Label(f0, image=bg).place(x="0", y="0", relwidth="1", relheight="1")
    Label(f0, text="Text And Audio Processing",
          font="comicsansms 30 bold", fg="lightblue").grid(padx=10)
    Label(f0, text=" GUI Application",
          font="comicsansms 30 bold", fg="lightblue").grid()
    f1 = Frame(f0, width="533")
    f1.grid(pady="10")

    l1 = Label(f1, text="Audio To Text", font="Times 20 bold")
    l1.grid()
    l2 = Label(
        f1, text="Audio To Text lets you process audio files or voices to text files", font="Times 10 bold")
    l2.grid()
    bt1 = Button(f1, text="Voice", command=attfpage,
                 font=("comicsansms", "10"))
    bt1.grid(pady="5")
    bt1 = Button(f1, text="Audio File", command=attf1,
                 font=("comicsansms", "10"))
    bt1.grid(pady="5")

    l3 = Label(f1, text="Text To Audio", font="Times 20 bold")
    l3.grid(padx="35")
    l4 = Label(
        f1, text="Text To Audio lets you process Text files to Audio files", font="Times 10 bold")
    l4.grid(padx="35")
    bt01 = Button(f1, text="Type", command=ttaf, font=("comicsansms", "10"))
    bt01.grid(pady="5", padx="35")
    bt01 = Button(f1, text="Text File", command=ttaf1,
                  font=("comicsansms", "10"))
    bt01.grid(pady="5", padx="35")

    l5 = Label(f1, text="Language Translator", font="Times 20 bold")
    l5.grid(padx="35")
    l6 = Label(f1, text="Translate one language to another",
               font="Times 10 bold")
    l6.grid(padx="35")
    bt2 = Button(f1, text="Open", command="", font=("comicsansms", "10"))
    bt2.grid(pady="5", padx="35")

    bt00 = Button(f0, text="Exit", command=exit, font=("comicsansms", "10"))
    bt00.grid(pady="5", padx="35")


mainpage()
f3.mainloop()
