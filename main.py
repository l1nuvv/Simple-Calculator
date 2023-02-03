from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except UserWarning:
        equation.set("error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    window = Tk()
    window.geometry("350x350")
    window.attributes('-alpha', 0.9)
    window.title("Calculator")

    equation = StringVar()

    expression_field = Entry(window, textvariable=equation, font=("bold", 15))
    expression_field.grid(columnspan=4, ipadx=70, ipady=20, sticky='')

    # buttons
    button1 = Button(window, text="1", fg="black", bg="grey",
                     command=lambda: press(1), height=3, width=6)
    button1.grid(row=5, column=0)

    button2 = Button(window, text="2", fg="black", bg="grey",
                     command=lambda: press(2), height=3, width=6)
    button2.grid(row=5, column=1)

    button3 = Button(window, text="3", fg="black", bg="grey",
                     command=lambda: press(3), height=3, width=6)
    button3.grid(row=5, column=2)

    button4 = Button(window, text=' 4 ', fg='black', bg='grey',
                     command=lambda: press(4), height=3, width=6)
    button4.grid(row=4, column=0)

    button5 = Button(window, text=' 5 ', fg='black', bg='grey',
                     command=lambda: press(5), height=3, width=6)
    button5.grid(row=4, column=1)

    button6 = Button(window, text=' 6 ', fg='black', bg='grey',
                     command=lambda: press(6), height=3, width=6)
    button6.grid(row=4, column=2)

    button7 = Button(window, text=' 7 ', fg='black', bg='grey',
                     command=lambda: press(7), height=3, width=6)
    button7.grid(row=3, column=0)

    button8 = Button(window, text=' 8 ', fg='black', bg='grey',
                     command=lambda: press(8), height=3, width=6)
    button8.grid(row=3, column=1)

    button9 = Button(window, text=' 9 ', fg='black', bg='grey',
                     command=lambda: press(9), height=3, width=6)
    button9.grid(row=3, column=2)

    button0 = Button(window, text=' 0 ', fg='black', bg='grey',
                     command=lambda: press(0), height=3, width=6)
    button0.grid(row=6, column=1)

    plus = Button(window, text=' + ', fg='black', bg='grey',
                  command=lambda: press("+"), height=3, width=6)
    plus.grid(row=6, column=3)

    minus = Button(window, text=' - ', fg='black', bg='grey',
                   command=lambda: press("-"), height=3, width=6)
    minus.grid(row=5, column=3)
    multiply = Button(window, text=' * ', fg='black', bg='grey',
                      command=lambda: press("*"), height=3, width=6)
    multiply.grid(row=4, column=3)

    divide = Button(window, text=' / ', fg='black', bg='grey',
                    command=lambda: press("/"), height=3, width=6)
    divide.grid(row=3, column=3)

    equal = Button(window, text=' = ', fg='black', bg='grey',
                   command=equalpress, height=3, width=6)
    equal.grid(row=8, column=3)

    clear = Button(window, text='Clear', fg='black', bg='grey',
                   command=clear, height=3, width=6)
    clear.grid(row=6, column='0')

    Decimal = Button(window, text='.', fg='black', bg='grey',
                     command=lambda: press('.'), height=3, width=6)
    Decimal.grid(row=6, column=2)


window.mainloop()
