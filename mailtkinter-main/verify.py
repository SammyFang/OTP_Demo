import sys
from tkinter import messagebox

from tkinter import *
import time

b=sys.argv[1]
f1=open("otp.txt","r")
b1=f1.read()
f1.close()
#print(b,b1)
if b==b1:
    f = open("status.txt", "w")
    f.write("成功")
    f.close()
    Window = Tk()
    Window.geometry("340x150")
    Window.title("成功")
    messagebox.showinfo("驗證正確", "OTP驗證成功!")
    Window.destroy()
    Window.mainloop()
else:
    f = open("status.txt", "w")
    f.write("failure")
    f.close()
