import tkinter as tk
root = tk.Tk()
entru =tk.Entry(root,width=14,bg="white",fg="black",borderwidth=5).grid(row=0,column=0,columnspan=10)
def Click(S):
    curent=entru.get()
    entru.insert(0,curent+S)
Button1=tk.Button(root,text="1",command=Click("1"),fg="red",bg="white").grid(row=2,column=0)
Button2=tk.Button(root,text="2",command=Click("2"),fg="red",bg="white").grid(row=2,column=1)
Button3=tk.Button(root,text="3",command=Click("3"),fg="red",bg="white").grid(row=2,column=2)
Button4=tk.Button(root,text="4",command=Click("4"),fg="red",bg="white").grid(row=3,column=0)
Button5=tk.Button(root,text="5",command=Click("5"),fg="red",bg="white").grid(row=3,column=1)
Button6=tk.Button(root,text="6",command=Click("6"),fg="red",bg="white").grid(row=3,column=2)
Button7=tk.Button(root,text="7",command=Click("7"),fg="red",bg="white").grid(row=4,column=0)
Button8=tk.Button(root,text="8",command=Click("8"),fg="red",bg="white").grid(row=4,column=1)
Button9=tk.Button(root,text="9",command=Click("9"),fg="red",bg="white").grid(row=4,column=2)
Button9=tk.Button(root,text="0",command=Click("0"),fg="red",bg="white").grid(row=5,column=1)
Button10=tk.Button(root,text="C",command=Click,fg="red",bg="white").grid(row=2,column=3)
Button11=tk.Button(root,text="=",command=Click,fg="red",bg="white").grid(row=2,column=4)
Button12=tk.Button(root,text="+",command=Click,fg="red",bg="white").grid(row=3,column=3)
Button13=tk.Button(root,text="-",command=Click,fg="red",bg="white").grid(row=3,column=4)
Button14=tk.Button(root,text="*",command=Click,fg="red",bg="white").grid(row=4,column=3)
Button15=tk.Button(root,text="/",command=Click,fg="red",bg="white").grid(row=4,column=4)
root.mainloop()