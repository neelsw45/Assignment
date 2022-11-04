from graphlib import TopologicalSorter
from tkinter import messagebox
from tkinter import*
from turtle import right

# top=Tk()
# top.geometry("200x100")

# def fun():
#     messagebox.showinfo("hello","Red button clicked")

# b1=Button(top,text="Red",Command=fun,activateforeground="Red" ,activebackground="pink",pady=10)
# b2=Button(top,text="Blue",Command=fun,activateforeground="Blue" ,activebackground="pink",pady=10)
# b3=Button(top,text="Green",Command=fun,activateforeground="Green" ,activebackground="pink",pady=10)
# b4=Button(top,text="Yellow",Command=fun,activateforeground="Yellow" ,activebackground="pink",pady=10)

# b1.pack(side=LEFT)
# b2.pack(side=RIGHT)
# b1.pack(side=TOP)
# b1.pack(side=BOTTOM)

top=Tk()
top.geometry("200*100")

def fun():
    messagebox.showinfo("hello","clicked red button")

    b1=Button(top,text="red",command=fun,activebackground="red",activeforeground="pink",pdpy=10)
    b2=Button(top,text="blue",command=fun,activebackground="blue",activeforeground="pink",pdpy=10)
    b3=Button(top,text="green",command=fun,activebackground="green",activeforeground="pink",pdpy=10)
    b4=Button(top,text="yellow",command=fun,activebackground="yellow",activeforeground="pink",pdpy=10)

top.mainloop()
