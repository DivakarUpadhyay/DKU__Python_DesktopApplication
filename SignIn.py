from tkinter import *
from PIL import ImageTk #PIL: Python Image Library

#DivakarUpadhyay Functionality Part
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

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold')
              ,bg='white',fg='firebrick1')
heading.place(x=605,y=120)

#Divakr Upadhyay UserName Field Creation Start
usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',13,'bold')
                    ,bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(1,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=588,y=222)
#Divakar Upadhyay UserName Field Creation End

#Divakr Upadhyay Password Field Creation Start
passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',13,'bold')
                    ,bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(1,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=588,y=282)

openeye=PhotoImage(file='DKU__Python_DesktopApplication\openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

#Divakr Upadhyay Password Field Creation End

login_window.mainloop()

