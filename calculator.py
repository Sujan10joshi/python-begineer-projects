from tkinter import *

win = Tk()
win.title('Simple Calculator')


calc_entry = Entry(win, width=35, borderwidth=5, font=('arial',10,'bold'), bg="#74baf2", justify='right')
calc_entry.grid(row=0, column=0, columnspan=4)

def on_click(number):
    current_value = calc_entry.get()
    calc_entry.delete(0, END)
    calc_entry.insert(0, str(current_value) + str(number))

def clear_btn():
    calc_entry.delete(0, END)

def button_equal():
    second_num = calc_entry.get()
    calc_entry.delete(0, END)
    if math == 'addition':
        calc_entry.insert(0, f_num + float(second_num))
    if math == 'subtraction':
        calc_entry.insert(0, f_num - float(second_num))
    if math == 'multiply':
        calc_entry.insert(0, f_num * float(second_num))
    if math == 'division':
        calc_entry.insert(0, f_num / float(second_num))
    if math == 'modulo':
        calc_entry.insert(0, f_num % float(second_num))
    


def button_add():
    first_num = calc_entry.get()
    calc_entry.delete(0, END)
    global f_num
    global math
    math = "addition"
    f_num = float(first_num)
    calc_entry.delete(0, END)


def button_subtract():
    first_num = calc_entry.get()
    calc_entry.delete(0, END)
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_num)
    calc_entry.delete(0,END)

def button_multiply():
    first_num = calc_entry.get()
    calc_entry.delete(0, END)
    global f_num
    global math
    math = "multiply"
    f_num = float(first_num)
    calc_entry.delete(0,END)

def button_division():
    first_num = calc_entry.get()
    calc_entry.delete(0, END)
    global f_num
    global math
    math = "division"
    f_num = float(first_num)
    calc_entry.delete(0,END)

def button_modulo():
    first_num = calc_entry.get()
    calc_entry.delete(0, END)
    global f_num
    global math
    math = "modulo"
    f_num = float(first_num)
    calc_entry.delete(0,END)



def action():
    return

# row 1
button_clear = Button(win, text='Clear', padx=40, pady=10, bg='#ed4134', command=lambda : clear_btn())
button_modulo = Button(win, text='%', padx=18, pady=10, bg='#4764b5', command=button_modulo)
button_division = Button(win, text='/', padx=21, pady=10, bg='#4764b5', command=button_division)
# row 2
button_7 = Button(win, text='7', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(7))
button_8 = Button(win, text='8', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(8))
button_9 = Button(win, text='9', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(9))
button_multiply = Button(win, text='x', padx=20, pady=10, bg='#4764b5', command=button_multiply)
# row 3
button_4 = Button(win, text='4', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(4))
button_5 = Button(win, text='5', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(5))
button_6 = Button(win, text='6', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(6))
button_subtract = Button(win, text='-', padx=21, pady=10, bg='#4764b5', command=button_subtract)
#row 4
button_1 = Button(win, text='1', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(1))
button_2 = Button(win, text='2', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(2))
button_3 = Button(win, text='3', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(3))
button_add = Button(win, text='+', padx=20, pady=10, bg='#4764b5', command=button_add)
#row 5

button_0 = Button(win, text='0', padx=20, pady=10, bg='#cad45d', command=lambda : on_click(0))
button_decimal = Button(win, text='.', padx=21, pady=10, bg='#cad45d', command=lambda : on_click('.'))
button_equal = Button(win, text='=', padx=51, pady=10, command=button_equal, bg='#42ed39')

# show on the screen, grid
button_clear.grid(row=1, column=0, columnspan=2)
button_modulo.grid(row=1, column=2)
button_division.grid(row=1, column=3)

button_9.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_7.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_6.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_4.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_3.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_1.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_decimal.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=2)




win.mainloop()