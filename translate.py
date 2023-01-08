from tkinter import *
from tkinter.ttk import Combobox
from newtrans import Mytranslator
root5=Tk()
root5.geometry('350x520')
root5.title('Google Translate')
root5.config(bg="blue")

def get():
    s=cmb001.get()
    d=cmb002.get()
    message= t01.get(1.0,END)
    translator=Mytranslator()
    text=translator.run(txt=message,src=s,dest=d)
    t02.delete(1.0,END)
    t02.insert(END,text)


f01=Frame(root5)
f01.grid()
l01=Label(root5,text="Google Translate",font="Times 15 bold",bg="green",fg="orange",width=29,height=2)
l01.grid(row=0,column=0)
t01=Text(root5,font="Times 10 italic",height=11,width=50,wrap=WORD)
t01.grid(row=1,column=0,pady=20)
langs=Mytranslator().langs
cmb001=Combobox(root5,values=langs,width=10)
cmb001.place(x=20,y=275)
cmb001.set('English')
bt001=Button(root5,text="Translate",font=("arial",10,'bold'),fg='red',bg='blue',activebackground='green',relief=GROOVE,command=get)
bt001.place(x=130,y=272)
cmb002=Combobox(root5,values=langs,width=10)
cmb002.set('Marathi')
cmb002.place(x=230,y=275)
t02=Text(root5,font="Times 10 italic",height=11,width=50,wrap=WORD)
t02.grid(pady=70)




root5.mainloop()