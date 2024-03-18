from tkinter import*
root = Tk()
def Click():
    Label1.pack()
Label1 = Label(root, text="Конпку нажали")
Button1=Button(root,text="Нажми",command=Click,fg="red",bg="green")
Button1.pack()

root.mainloop()