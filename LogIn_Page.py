from tkinter import *

def login():
   root = Tk()
   root.geometry('1300x720')
   root.title("Registration Form")
   label_0 = Label(root, text="Sign In",width=20,font=("bold", 40))
   label_0.place(x=260,y=55)
   label_1 = Label(root, text="Username : ",width=20,font=("bold", 10))
   label_1.place(x=350,y=200)
   entry_1 = Entry(root,width=48)
   entry_1.place(x=550,y=200)
   label_2 = Label(root, text="Password : ",width=20,font=("bold", 10))
   label_2.place(x=350,y=250)
   entry_2 = Entry(root,width=48)
   entry_2.place(x=550,y=250)
   Button(root, text='Log In',width=80,bg='brown',fg='white').place(x=350,y=400)
   root.mainloop()

#login()



