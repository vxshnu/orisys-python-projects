import tkinter
window=tkinter.Tk()
window.title("Calculator")
window.geometry("400x400")
window.config(bg="black")

first=tkinter.Label(text="",bg="black",foreground="white",font=("timesnewroman 20"))
first.grid(row=0,column=0)

numbers=[]
expression=""

def on_click(button_id):
    global numbers,expression
    #if not numbers: 
    #    numbers.append(0) 
    if button_id in '0123456789':
        expression+=button_id
        #numbers[i].append(button_id)
    elif button_id in '+-*/':
        expression+=" "
        expression+=button_id
        expression+=" "
        #numbers[i]=button_id
        first.config(text=f"{expression}")
    elif button_id == '=':
        #result=int(numbers[start])
        numbers=expression.split()
        print(numbers)
        a=0
        result=0
        for i in range(len(numbers)):
            print(i)
            if numbers[i]=='+':
                result=int(numbers[i-1])+int(numbers[i+1])
            elif numbers[i]=='-':
                result=int(numbers[i-1])-int(numbers[i+1])
            elif numbers[i]=='*':
                result=int(numbers[i-1])*int(numbers[i+1])
            elif numbers[i]=='/':
                result=int(numbers[i-1])/int(numbers[i+1])
        first.config(text=f"{result}")

one=tkinter.Button(text="1",height=5,width=12,command=lambda:on_click('1'))
two=tkinter.Button(text="2",height=5,width=12,command=lambda:on_click('2'))
three=tkinter.Button(text="3",height=5,width=12,command=lambda:on_click('3'))
four=tkinter.Button(text="4",height=5,width=12,command=lambda:on_click('4'))
five=tkinter.Button(text="5",height=5,width=12,command=lambda:on_click('5'))
six=tkinter.Button(text="6",height=5,width=12,command=lambda:on_click('6'))
seven=tkinter.Button(text="7",height=5,width=12,command=lambda:on_click('7'))
eight=tkinter.Button(text="8",height=5,width=12,command=lambda:on_click('8'))
nine=tkinter.Button(text="9",height=5,width=12,command=lambda:on_click('9'))
zero=tkinter.Button(text="0",height=5,width=12,command=lambda:on_click('0'))
add=tkinter.Button(text="+",height=5,width=12,command=lambda:on_click('+'))
sub=tkinter.Button(text="-",height=5,width=12,command=lambda:on_click('-'))
mul=tkinter.Button(text="*",height=5,width=12,command=lambda:on_click('*'))
div=tkinter.Button(text="/",height=5,width=12,command=lambda:on_click('/'))
equal=tkinter.Button(text="=",height=5,width=12,command=lambda:on_click('='))
dot=tkinter.Button(text=".",height=5,width=12,command=lambda:on_click('.'))

one.grid(row=1,column=0)
two.grid(row=1,column=1)
three.grid(row=1,column=2)
four.grid(row=2,column=0)
five.grid(row=2,column=1)
six.grid(row=2,column=2)
seven.grid(row=3,column=0)
eight.grid(row=3,column=1)
nine.grid(row=3,column=2)
zero.grid(row=4,column=1)
add.grid(row=1,column=3)
sub.grid(row=2,column=3)
mul.grid(row=3,column=3)
div.grid(row=4,column=3)
equal.grid(row=4,column=0)
dot.grid(row=4,column=2)

for i in range(5):
    window.grid_rowconfigure(i, weight=1)

for j in range(4):
    window.grid_columnconfigure(j, weight=1)
    
window.mainloop()