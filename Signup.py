from ctypes import alignment
from tkinter import *
from turtle import color
from PIL import ImageTk
from matplotlib.widgets import CheckButtons #PIL: Python Image Library

def login_page():
    signup_window.destroy()
    import SignIn
#DivakarUpadhyay GUI Part
signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file='DKU__Python_DesktopApplication\\backgroundimage.jpg')
bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',15,'bold')
              ,bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25)

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25)

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25)

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25)

confirmpasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',9,'bold'),
                                  fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2')
termsandconditions.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,fg='white',bg='firebrick1'
                    ,activebackground='firebrick1',activeforeground='white',width=17)
signupButton.grid(row=10,column=0)

#Divakar Upadhyay SignUp Label Creation Start
alreadyanccount=Label(frame,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
alreadyanccount.grid(row=11,column=0,sticky='w',padx=25,pady=20)
#Divakar Upadhyay SignUp Label Creation End

#Divakar Upadhyay newaccount Label Creation Start
loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),
                   fg='blue',bg='white',activebackground='white',
                   activeforeground='blue',cursor='hand2',bd=0,command=login_page)
loginButton.place(x=170,y=350)
#Divakar Upadhyay newaccount Label Creation Start


signup_window.mainloop() #helps to see the window i.e window will pop up

