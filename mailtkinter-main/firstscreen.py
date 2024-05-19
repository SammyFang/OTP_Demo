import os
from tkinter import *
from tkinter import messagebox
Window=Tk()
Window.geometry('480x150')
Window.title("OTP驗證")
def verify():
    cmd=str(a.get())
    temp='python sendmail.py'+' '+cmd
    os.system(temp)
label1=Label(Window,text="OTP_測試用",relief="solid",font=("arial",13,"bold"),fg='blue').pack(fill=BOTH)
a=StringVar()
Re=Label(Window,text="電子信箱：",font=("arial",13,"bold")).place(x=0,y=50)
w=Entry(Window,width=50,validate="key",textvariable=a)
w.place(x=100,y=50)
log = Button(Window, text="測試",relief="raised", bg='green', font=("arial", 13, "bold"), fg='black',command=verify).place(x=200,y=100)
Window.mainloop()
