from tkinter import *

root=Tk()
tFrame=Frame(root)
bFrame=Frame(root)

tFrame.pack()
bFrame.pack(side=BOTTOM)

btn1=Button(tFrame,text="first button",fg="green")
btn2=Button(tFrame,text="second button",fg="blue")
btn3=Button(tFrame,text="third button",fg="red")
btn4=Button(bFrame,text="four button",fg="cyan")
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=BOTTOM)

root.mainloop()


