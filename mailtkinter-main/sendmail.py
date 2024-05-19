import os,math
import random,sys
import smtplib
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
mailid=sys.argv[1]
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg=str("OPT驗證碼為："+OTP+"\n"+"注意!! 請在2分鐘內輸入以免失效").encode("utf-8")
file2=open("otp.txt","w")
file2.write(OTP)
file2.close()
# &&&&&&&&&&&&- Your mail id. SENDING OTP FROM mail id
# ************- Your app password. If you do not know how to generate app password for your mail please google.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("&&&&&&&&&&&&-", "************-")
print(msg)
s.sendmail('&&&&&&&&&&&&-&',mailid,msg)

os.system('python second.py')
