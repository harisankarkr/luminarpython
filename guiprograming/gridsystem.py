from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("first prg")

import mysql.connector
from dbconnectprgm.dbconnet import get_connection
def db_connect(username,password):
    print("inside.........")
    db=get_connection()
    cursor=db.cursor()
    try:
        cursor.execute(("select * from users where username=%s and password=%s"),(username,password))
        user=cursor.fetchone()
        return user

    except Exception as e:
        print(e.args)

def authenticate_user():
    uname=uentry.get()
    pwd=pentry.get()
    user=db_connect(uname,pwd)
    if (user==None):
        messagebox.showerror("login failed","error")
    else:
        messagebox.showinfo("login successfully","welcome")

ulabel=Label(root,text="username")
plabel=Label(root,text="password")
uentry=Entry(root)
pentry=Entry(root)

btn=Button(root,text="login",command=authenticate_user)

ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)
btn.grid(row=2,column=1)

root.mainloop()