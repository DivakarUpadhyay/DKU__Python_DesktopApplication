from tkinter import *
from PIL import ImageTk
root=Tk()
root.geometry('990x660+50+50')
bgImage=ImageTk.PhotoImage(file='backgroundimage.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

root.mainloop()

