from ctypes import alignment
from tkinter import *
from turtle import color
from PIL import ImageTk #PIL: Python Image Library
from tkinter import messagebox
import pymysql
import sys


def clear():
    usernameEntry.delete(0,END)
    usernameEntry.insert(1,'Username')
    passwordEntry.delete(0,END)
    passwordEntry.insert(1,'Password')
#DivakarUpadhyay Functionality Part
def signup_page():
    login_window.destroy()
    import Signup

def login_user():

    if usernameEntry.get()=='' or passwordEntry.get()=='':
       messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
           con=pymysql.connect(host='localhost',user='root',passwd='123456')
           mycursor=con.cursor()
        except :
          messagebox.showerror('Error','Connecton is not established try again')
          return
        query="use registeruser"
        mycursor.execute(query)
        query='select * from userinformation where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
        clear()
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)    

def hide():
    openeye.config(file='DKU__Python_DesktopApplication\closeye.png')    
    passwordEntry.config(show='*')
    eyeButton.config(command=show)  

def show():
    openeye.config(file='DKU__Python_DesktopApplication\openeye.png')    
    passwordEntry.config(show='')
    eyeButton.config(command=hide)              


#DivakarUpadhyay GUI Part
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')

image = ImageTk.Image.open(r"DKU__Python_DesktopApplication\backgroundimage.jpg")
bgImage=ImageTk.PhotoImage(image)
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',15,'bold')
              ,bg='white',fg='firebrick1')
heading.place(x=605,y=120)

#Divakr Upadhyay UserName Field Creation Start
usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',10,'bold')
                    ,bd=0,fg='#5da924')
usernameEntry.place(x=590,y=200)
usernameEntry.insert(1,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=588,y=222)
#Divakar Upadhyay UserName Field Creation End

#Divakr Upadhyay Password Field Creation Start
passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',10,'bold')
                    ,bd=0,fg='#5da924')
passwordEntry.place(x=590,y=260)
passwordEntry.insert(1,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=588,y=282)
#Divakar Upadhyay Password Field Creation End

#Divakar Upadhyay eye Button Creation Start
openeye=PhotoImage(file='DKU__Python_DesktopApplication\openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)
#Divakar Upadhyay eye Button Creation End

#Divakar Upadhyay forget Button Creation Start
forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',activeforeground='firebrick1')
forgetButton.place(x=715,y=295)
#Divakar Upadhyay forget Button Creation End

#Divakar Upadhyay Login Button Creation Start
loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1',activebackground='white',
                   activeforeground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)
#Divakar Upadhyay Login Button Creation End

#Divakar Upadhyay OR Label Creation Start
orLabel=Label(login_window,text='---------------OR--------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)
#Divakar Upadhyay OR Label Creation End

#Divakar Upadhyay Social Media Label Creation Start
facebook_logo=PhotoImage(file='DKU__Python_DesktopApplication\\facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file='DKU__Python_DesktopApplication\google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='DKU__Python_DesktopApplication\\twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)
#Divakar Upadhyay Social Media Label Creation End

#Divakar Upadhyay SignUp Label Creation Start
signupLabel=Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=590,y=500)
#Divakar Upadhyay SignUp Label Creation End

#Divakar Upadhyay newaccount Label Creation Start
newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),
                   fg='blue',bg='white',activebackground='white',
                   activeforeground='blue',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)
#Divakar Upadhyay newaccount Label Creation Start


login_window.mainloop() #helps to see the window i.e window will pop up

