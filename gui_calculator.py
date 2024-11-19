from tkinter import *

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except Exception as e:
        equation.set("Error: " + str(e))
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="dark blue")
    gui.title("Simple Calculator")
    gui.geometry("270x170")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    buttons = [
        [1, 2, 3, "+"], 
        [4, 5, 6, "-"], 
        [7, 8, 9, "*"],
        [0, ".", "=", "/"]
    ]

    for row in range(4):
        for col in range(4):
            if buttons[row][col] == "=":
                button = Button(gui, text=str(buttons[row][col]), fg="black", bg="gray", command=equalpress, height=1, width=7)
            else:
                button = Button(gui, text=str(buttons[row][col]), fg="black", bg="gray", command=lambda num=buttons[row][col]: press(num), height=1, width=7)
            button.grid(row=row+2, column=col)
    
    btn_clr = Button(gui, text="Clear", fg="black", bg="gray", command=clear)
    btn_clr.grid(row=6, columnspan=4, ipadx=70)

    gui.mainloop()