from tkinter import *

root=Tk()
root.title("first prg")

label1=Label(root,text="name")
label1.pack()
entry1=Entry(root)
entry1.pack()

label2=Label(root,text="email")
label2.pack()
entry2=Entry(root)
entry2.pack()

label3=Label(root,text="password")
label3.pack()
entry3=Entry(root)
entry3.pack()

root.mainloop()