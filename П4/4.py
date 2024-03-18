from tkinter import*
root = Tk()
e=Entry(root,width=50,bg="white",fg="black",borderwidth=5)
e.pack()
e.insert(0,"Enter Your Name")
def Click():
    Hi="Hi "+e.get()
    Label1 = Label(root, text=Hi)
    Label1.pack()
Button1=Button(root,text="Нажми после записи имени",command=Click,fg="red",bg="green")
Button1.pack()

root.mainloop()