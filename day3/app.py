import tkinter

def print_hello():
    print("Hi, You clicked me!")

def on_click():
    labell.config(text="GM")
    
window=tkinter.Tk()
window.title("First App")
window.minsize(700,500)

labell=tkinter.Label(text="Hello World!")
labell.pack()

label2=tkinter.Label(text="Hello World!",font=("timesnewroman 20 bold"),bg=("green"),foreground=("white"))
label2.place(x=250,y=250)

w = tkinter.Button (text="Click Me",height=0, width=10,command=on_click,bg="red",foreground=("white"))
w.place(x=300,y=200)

window.mainloop()

