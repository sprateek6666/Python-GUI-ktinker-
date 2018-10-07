from tkinter import *
from tkinter import messagebox

import LogIn_Page
import SignUp_Page
import Consignment_Tracking


top = Tk()
top.title("Courier Management System")
top.geometry("1300x720")
top.configure(bg='#d1d1d1')

label_1 = Label(top, text="LOVELY PROFESSIONAL UNIVERSITY",width=40,font=("bold", 30))
label_1.place(x=65,y=50)
label_1.config(background='#d1d1d1')

label_2 = Label(top, text="COURIER MANAGEMENT SYSTEM",width=40,font=("bold", 30))
label_2.place(x=65,y=170)
label_2.config(background='#d1d1d1')

A = Button(top, text = "Existing User  (Log In Here)", command = LogIn_Page.login,height = 3, width = 50)
A.place(x = 440,y = 300)
B = Button(top, text = "New User  (Sign Up Here)", command = SignUp_Page.signup,height = 3, width = 50)
B.place(x = 440,y = 400)
C = Button(top, text = "Track Consignment", command = Consignment_Tracking.consignment,height = 3, width = 50)
C.place(x = 440,y = 500)

top.mainloop()
