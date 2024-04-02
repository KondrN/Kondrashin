from tkinter import*
root = Tk()
first_num=0
math=0
e=Entry(root,width=20, borderwidth=3,bg="white",fg="black")
e.grid(row=0, column=0, columnspan=4, padx=1, pady=0)
def button_click(num):
    en=e.get()+num
    e.delete(0,100)
    e.insert(0,en)
def button_add():
    global first_num
    global math
    math="+"
    first_num=e.get()
    e.delete(0,100)
def button_min():
    global first_num
    global math
    math = "-"
    first_num=e.get()
    e.delete(0,100)
def button_umn():
    global first_num
    global math
    math = "*"
    first_num=e.get()
    e.delete(0,100)
def button_del():
    global first_num
    global math
    math = "/"
    first_num=e.get()
    e.delete(0,100)
def button_ravn():
    global first_num
    global math
    if (math=="+"):
        itog=int(first_num)+int(e.get())
        e.delete(0, 100)
        e.insert(0,itog)
    if (math=="-"):
        itog=int(first_num)-int(e.get())
        e.delete(0, 100)
        e.insert(0,itog)
    if (math=="*"):
        itog=int(first_num)*int(e.get())
        e.delete(0, 100)
        e.insert(0,itog)
    if (math=="/"):
        itog=int(first_num)/int(e.get())
        e.delete(0, 100)
        e.insert(0,int(itog))
def Clear():
    e.delete(0, 100)
#Создаём кнопки цифр
Button1=Button(root,text="1",command=lambda s="1": button_click(s),fg="red",bg="green").grid(row=1, column=0)
Button2=Button(root,text="2",command=lambda s="2": button_click(s),fg="red",bg="green").grid(row=1, column=1)
Button3=Button(root,text="3",command=lambda s="3": button_click(s),fg="red",bg="green").grid(row=1, column=2)
Button4=Button(root,text="4",command=lambda s="4": button_click(s),fg="red",bg="green").grid(row=2, column=0)
Button5=Button(root,text="5",command=lambda s="5": button_click(s),fg="red",bg="green").grid(row=2, column=1)
Button6=Button(root,text="6",command=lambda s="6": button_click(s),fg="red",bg="green").grid(row=2, column=2)
Button7=Button(root,text="7",command=lambda s="7": button_click(s),fg="red",bg="green").grid(row=3, column=0)
Button8=Button(root,text="8",command=lambda s="8": button_click(s),fg="red",bg="green").grid(row=3, column=1)
Button9=Button(root,text="9",command=lambda s="9": button_click(s),fg="red",bg="green").grid(row=3, column=2)
Button0=Button(root,text="0",command=lambda s="0": button_click(s),fg="red",bg="green").grid(row=4, column=1)
ButtonC=Button(root,text="C",command = Clear,fg="red",bg="green").grid(row=4, column=0)
ButtonRav=Button(root,text="=", command=button_ravn,fg="red",bg="green").grid(row=4, column=2)
ButtonPlus=Button(root,text="+",command=button_add,fg="red",bg="green").grid(row=1, column=3)
ButtonMinus=Button(root,text="-",command=button_min,fg="red",bg="green").grid(row=2, column=3)
ButtonUmn=Button(root,text="*",command=button_umn,fg="red",bg="green").grid(row=3, column=3)
ButtonDel=Button(root,text="/",command=button_del,fg="red",bg="green").grid(row=4, column=3)

root.mainloop()