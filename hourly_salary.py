""" tkinter module gives us graphical user interphase"""
from tkinter import Tk, Label, Entry, END, Button

root = Tk()
root.geometry("500x600")
root.title("Hourly Salary Calculator")
root.config(bg="#D14D72")


def cal():
    """ Calculate Per hour rate"""
    sal = int(salary.get())
    hrs = int(hours.get())
    hrs = hrs*5*52  # hours worked in whole year
    res = round(sal/hrs)
    res = "Your Worth is  " + str(res) + "  ₹ Per Hour"
    result.config(text=res)


def temp_sal(arg):
    '''Erase the default text when you click on the text entry field'''
    salary.delete(0, 'end')


def temp_hour(arg):
    '''Erase the default text when you click on the text entry field'''
    hours.delete(0, 'end')


heading = Label(root, text="Salary Calculator", bg="#800f2f",
                fg='#fff0f3', font=('Times new roman', 30, 'bold'))
heading.place(x=0, y=20, width=500, height=100)

salary = Entry(root, font=('verdana', 17, 'bold'), bg='#FCC8D1', fg='#590d22')
salary.place(x=20, y=170, width=460, height=30)
salary.insert(END, "Enter your CTC")
salary.bind("<FocusIn>", temp_sal)

hours = Entry(root, font=('verdana', 17, 'bold'), bg='#FCC8D1', fg='#590d22')
hours.place(x=20, y=240, width=460, height=30)
hours.insert(END, "Hours worked per day")
hours.bind("<FocusIn>", temp_hour)


calculate = Button(root, text="Calculate", border=10, font=(
    'verdana', 18, 'bold'), bg='#590d22', fg='#fff0f3', command=cal)
calculate.place(x=130, y=350, width=220, height=55)

result = Label(root, text="Result", bg="#ff7096",
               fg='#000814', font=('Times new roman', 22, 'bold'))
result.place(x=20, y=480, width=460, height=60)

footer = Label(root, text='Dedicated to Ayush Silarpuria',
               font=('Arial', 7), bg='#D14D72')
footer.place(x=200, y=580)

root.mainloop()
