from tkinter import *

def consignment():
	root = Tk()
	root.geometry('1300x720')
	root.title("Consignment Tracking")
	label_0 = Label(root, text="Consignment Tracking",width=20,font=("bold", 40))
	label_0.place(x=260,y=55)
	label_1 = Label(root, text="Mobile Number : ",width=20,font=("bold", 10))
	label_1.place(x=350,y=200)
	entry_1 = Entry(root,width=48)
	entry_1.place(x=550,y=200)
	label_2 = Label(root, text="Consignment Number : ",width=20,font=("bold", 10))
	label_2.place(x=350,y=250)
	entry_2 = Entry(root,width=48)
	entry_2.place(x=550,y=250)
	Button(root, text='Track Consignment',width=80,bg='brown',fg='white').place(x=340,y=350)
	root.mainloop()

#consignment()
