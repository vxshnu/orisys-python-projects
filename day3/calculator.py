import tkinter
window = tkinter.Tk()
window.title("Calculator")
window.geometry("380x380")
window.config(bg="black")

first = tkinter.Label(text="", bg="black", foreground="white", font=("timesnewroman 20"))
first.grid(row=0, column=0, columnspan=4)

numbers = []
expression = ""
result = 0

def on_click(button_id):
    global numbers, expression, result
    if button_id in '0123456789':
        expression += button_id
        txt = first.cget("text")
        first.config(text=f"{txt}{button_id}")
    elif button_id in '+-*/':
        expression += f" {button_id} "
        first.config(text=expression)
    elif button_id == '=':
        numbers = expression.split()
        result = float(numbers[0])
        for i in range(1, len(numbers), 2):
            operator = numbers[i]
            operand = float(numbers[i + 1])
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                result /= operand
        first.config(text=f"{result}")
        expression = str(result)
        numbers = []
    elif button_id == 'C':
        numbers = []
        expression=""
        first.config(text="")

one = tkinter.Button(text="1", height=5, width=12, command=lambda: on_click('1'))
two = tkinter.Button(text="2", height=5, width=12, command=lambda: on_click('2'))
three = tkinter.Button(text="3", height=5, width=12, command=lambda: on_click('3'))
four = tkinter.Button(text="4", height=5, width=12, command=lambda: on_click('4'))
five = tkinter.Button(text="5", height=5, width=12, command=lambda: on_click('5'))
six = tkinter.Button(text="6", height=5, width=12, command=lambda: on_click('6'))
seven = tkinter.Button(text="7", height=5, width=12, command=lambda: on_click('7'))
eight = tkinter.Button(text="8", height=5, width=12, command=lambda: on_click('8'))
nine = tkinter.Button(text="9", height=5, width=12, command=lambda: on_click('9'))
zero = tkinter.Button(text="0", height=5, width=12, command=lambda: on_click('0'))
add = tkinter.Button(text="+", height=5, width=12, command=lambda: on_click('+'))
sub = tkinter.Button(text="-", height=5, width=12, command=lambda: on_click('-'))
mul = tkinter.Button(text="*", height=5, width=12, command=lambda: on_click('*'))
div = tkinter.Button(text="/", height=5, width=12, command=lambda: on_click('/'))
equal = tkinter.Button(text="=", height=5, width=12, command=lambda: on_click('='))
dot = tkinter.Button(text="C", height=5, width=12, command=lambda: on_click('C'))

one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
zero.grid(row=4, column=1)
add.grid(row=1, column=3)
sub.grid(row=2, column=3)
mul.grid(row=3, column=3)
div.grid(row=4, column=3)
equal.grid(row=4, column=0)
dot.grid(row=4, column=2)

for i in range(5):
    window.grid_rowconfigure(i, weight=1)

for j in range(4):
    window.grid_columnconfigure(j, weight=1)

window.mainloop()

