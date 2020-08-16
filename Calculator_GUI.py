"""
Created on Fri May 14 22:22:14 2020

@email_id : shubham.more26@gmail.com
@author: SHUBHAM MORE
"""

from tkinter import *
import tkinter as tk

# root declaration
root = Tk()
root.title('Calculator')
root.geometry('358x510')
root.resizable(FALSE, FALSE)
root.config(bg='#404040')
btn_font = 'console 20 '
root.iconphoto(FALSE, tk.PhotoImage(file='Apps-Calc-icon.png'))


# Display decoration


data = StringVar()
oprator = ''

display = Entry(root, bd=4, textvariable=data, borderwidth=9, width=16, insertwidth=5,
                font=('verdana '
                      '', 28), justify=RIGHT)
display.place(x=0, y=3)
display.config(state='disabled')
display.focus_set()


def clicked(expression):
    global oprator
    oprator = oprator + str(expression)
    data.set(oprator)


def calculate():
    global oprator
    try:
        values = data.get()
        values = eval(values)
        clear_display()
        data.set(values)
        oprator = str(values)
    except Exception as msg:
        data.set('Error')


def clear_display():
    global oprator
    data.set('')
    display.delete(0, END)
    oprator=''


# Buttons
clear = Button(root, command=clear_display, text='C', font='console 20 ', width=5, height=2)
clear.place(x=2, y=68)

one = Button(root, text='1', command=lambda: clicked(1), font=btn_font, width=5, height=2)
one.place(x=2, y=322 - 88 - 78)

four = Button(root, text='4', command=lambda: clicked(4), font=btn_font, width=5, height=2)
four.place(x=2, y=322 - 78)

mod = Button(root, text='%', command=lambda: clicked('%'), font=btn_font, width=5, height=2)
mod.place(x=92, y=68)

seven = Button(root, text='7', command=lambda: clicked(7), font=btn_font, width=5, height=2)
seven.place(x=2, y=332)

two = Button(root, text='2', command=lambda: clicked(2), font=btn_font, width=5, height=2)
two.place(x=92, y=156)

into = Button(root, text='*', command=lambda: clicked('*'), font=btn_font, width=5, height=2)
into.place(x=182, y=68)

three = Button(root, text='3', command=lambda: clicked(3), font=btn_font, width=5, height=2)
three.place(x=182, y=156)

div = Button(root, text='/', command=lambda: clicked('/'), font=btn_font, width=5, height=2)
div.place(x=272, y=68)

sub = Button(root, text='-', command=lambda: clicked('-'), font=btn_font, width=5, height=2)
sub.place(x=272, y=156)

five = Button(root, text='5', command=lambda: clicked(5), font=btn_font, width=5, height=2)
five.place(x=92, y=244)

six = Button(root, text='6', command=lambda: clicked(6), font=btn_font, width=5, height=2)
six.place(x=182, y=244)

add = Button(root, text='+', command=lambda: clicked('+'), font=btn_font, width=5, height=2)
add.place(x=272, y=244)

eight = Button(root, text='8', command=lambda: clicked(8), font=btn_font, width=5, height=2)
eight.place(x=92, y=332)

nine = Button(root, text='9', command=lambda: clicked(9), font=btn_font, width=5, height=2)
nine.place(x=182, y=332)

zero = Button(root, text='0', command=lambda: clicked(0), padx=72, font=btn_font, height=2)
zero.place(x=2, y=420)

dot = Button(root, text='.', command=lambda: clicked('.'), font=('console', 20, 'bold'), padx=28.5, pady=17)
dot.place(x=183, y=420)

eql = Button(root,command =calculate, highlightcolor='red', text='=', bg='orange', font=('console', 20), pady=62, padx=23.9)
eql.place(x=272, y=332)

mainloop()
