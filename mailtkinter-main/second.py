from tkinter import *
from tkinter import messagebox
import tkinter
import time
import  os
Window=Tk()
Window.geometry("340x150")
Window.title("OPT驗證")
count = 3  #global variable for count calculation. Initially there are 3 attempts. So I set as 3
def verify():
    global count
    global Window
    end=time.time()          # timers ends when the user clicks verfiy
    t = format(end - start)  # calculate the difference between end and start timer
    print(float(t))          #  print the time in seconds
    if float(t) >= 120:      # Check it the user enters above 2 minutes. So i set as >=120
        messagebox.showinfo("Time out", "Session Expired ...Time out Please regenerate OTP")
        Window.destroy()
    else:
        cmd1=str(a.get())             # Get the entered OTP
        cmd='python verify.py '+cmd1  
        os.system(cmd)                # call the verify program
        ok='嘗試輸入剩餘次數： '+str((count-1)) 
        count=count-1
        f1=open("status.txt","r")
        bh=f1.read()

        if count>=1 and bh != "成功":
            tkinter.messagebox.askretrycancel("失敗", ok)
            f1.close()

        elif count == 0 and bh != "成功":
            f=open("otp.txt","w")
            f.write("")
            f.close()
            messagebox.showinfo("失敗","超過嘗試輸入次數.請重新產生OTP")
            f1.close()
            Window.destroy()
        elif bh == "成功":
            f1.close()
            Window.destroy()

start=time.time() # Timer started once the screen is entered
label1=Label(Window,text="OPT驗證",relief="solid",font=("arial",13,"bold"),fg='blue').pack(fill=BOTH)
a=StringVar()
Re=Label(Window,text="輸入OPT：",font=("arial",13,"bold")).place(x=0,y=50)
w1=Entry(Window,width=30,textvariable=a)
w1.place(x=100,y=50)
Re1=Label(Window,text="請在2分鐘內輸入",font=("arial",10,"bold")).place(x=200,y=50)
ver = Button(Window, text="驗證",relief="raised", bg='blue', font=("arial", 13, "bold"), fg='white',command=verify).place(x=140,y=100)
Window.mainloop()
