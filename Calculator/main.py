import tkinter as tk
import math

button_values = [
    ['AC', '+/-', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '√', '=']
]

right_symbols = ['/', '*', '-', '+', '=', '√']
top_symbols = ['AC', '+/-', '%']

row_count = len(button_values)
column_count = len(button_values[0])

color_light_gray = '#D4D4D2'
color_black = '#1C1C1C'
color_dark_gray = '#505050'
color_orange = '#FF9500'
color_white = 'white'

window = tk.Tk()
window.title("Calculator")
window.iconphoto(True, tk.PhotoImage(file='calculator-2478633_1280.png'))
window.resizable(False, False)

frame = tk.Frame(window)

label = tk.Label(
    frame,
    text='0',
    font=('Arial', 45),
    bg=color_black,
    fg=color_white,
    anchor='e',
    width=column_count
)
label.grid(
    row=0,
    column=0,
    columnspan=column_count,
    sticky='we'
)

A = '0'
B = None
operator = None


def clear_all():
    global A, B, operator
    A = '0'
    B = None
    operator = None


def format_number(num):
    # show up to 5 decimals, remove trailing zeros and trailing dot
    return f"{num:.5f}".rstrip('0').rstrip('.')


def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == '=':
            if A is not None and operator is not None:
                B = label['text']
                numA = float(A)
                numB = float(B)

                if operator == '+':
                    label['text'] = format_number(numA + numB)
                elif operator == '-':
                    label['text'] = format_number(numA - numB)
                elif operator == '*':
                    label['text'] = format_number(numA * numB)
                elif operator == '/':
                    label['text'] = format_number(numA / numB)
                elif operator == '√':
                    # use only A for sqrt (unary)
                    label['text'] = format_number(math.sqrt(numA))

                clear_all()

        elif value in '+-*/√':
            if operator is None:
                A = label['text']
                label['text'] = '0'
                B = '0'
            operator = value

    elif value in top_symbols:
        if value == 'AC':
            clear_all()
            label['text'] = '0'
        elif value == '+/-':
            result = float(label['text']) * -1
            label['text'] = format_number(result)
        elif value == '%':
            result = float(label['text']) / 100
            label['text'] = format_number(result)

    else:
        if value == '.':
            if value not in label['text']:
                label['text'] += value
        elif value in '0123456789':
            if label['text'] == '0':
                label['text'] = value
            else:
                label['text'] += value


for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tk.Button(
            frame,
            text=value,
            font=('Arial', 30),
            width=column_count - 1,
            height=1,
            command=lambda value=value: button_clicked(value)
        )

        if value in top_symbols:
            button.config(fg=color_black, bg=color_light_gray)
        elif value in right_symbols:
            button.config(fg=color_white, bg=color_orange)
        else:
            button.config(fg=color_white, bg=color_dark_gray)

        button.grid(row=row + 1, column=column)

frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
