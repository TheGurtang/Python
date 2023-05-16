import csv
from tkinter import *
from tkinter import font


window = Tk()
window.title('Log-in Form')
tit1 = Label(window, text='Please, fill out the following form!', font=('Arial Bold', 13))
tit1.grid(row=0, column=0)


def make_dict():
    first_l = ['Login: ', 'Password: ', 'E-mail: ']
    sec_l = [a2_value.get(), b2_value.get(), c2_value.get()]                             ## !pay attention that '_value.get()' method is necessary for passing the data from the GUI to your CSV file!
    dic = dict(zip(first_l, sec_l))
    with open('got_data.csv', newline='', mode='a')as outcome:
        csv_w = csv.writer(outcome, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_w.writerow([dic])

a1 = Button(window, text='Enter your login: ', font=7)
a1.grid(row=1, column=0)

a2_value=StringVar()
a2 = Entry(window, textvariable=a2_value)
a2.grid(row=1, column=1)


b1 = Button(window, text='Enter your password: ', font=7)
b1.grid(row=2, column=0)

b2_value=StringVar()
b2 = Entry(window, textvariable=b2_value)
b2.grid(row=2, column=1)


c1 = Button(window, text='Enter your e-mail: ', font=7)
c1.grid(row=3, column=0)

c2_value=StringVar()
c2 = Entry(window, textvariable=c2_value)
c2.grid(row=3, column=1)


proc = Button(window, text='Submit', font=7, command=make_dict)
proc.grid(row=4, column= 2)


window.mainloop()
