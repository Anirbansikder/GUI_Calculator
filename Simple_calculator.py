from tkinter import *

root = Tk()

root.title("Simple Calculator")
root.iconbitmap(
    'F:\projects\Simple GUI Calculator\Martz90-Circle-Calculator.ico')

e = Entry(root, width=40, borderwidth=5)
e.insert(0, "Enter Your Expression")
e.grid(row=0, column=0, columnspan=4, padx=5, pady=10)
ch = '='


def addbtn(number):
    # e.delete(0,END)
    if(e.get() == "Dude , Seriously !! ERROR"):
        e.delete(0, END)
    if(e.get() == "Enter Your Expression"):
        e.delete(0, END)
    if(e.get() == "Clear And Try Again"):
        e.delete(0, END)
    if(e.get() == "0"):
        e.delete(0, END)

    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + str(number))


def clear():
    e.delete(0, END)
    e.insert(0, 0)


def add():
    if(e.get() == "Dude , Seriously !! ERROR" or e.get() == "Clear And Try Again"):
        e.delete(0, END)
        e.insert(0, "Clear And Try Again")
        return
    firstnum = e.get()
    global f_num
    global ch
    ch = '+'
    f_num = float(firstnum)
    e.delete(0, END)


def sub():
    if(e.get() == "Dude , Seriously !! ERROR" or e.get() == "Clear And Try Again"):
        e.delete(0, END)
        e.insert(0, "Clear And Try Again")
        return
    firstnum = e.get()
    global f_num
    global ch
    ch = '-'
    f_num = float(firstnum)
    e.delete(0, END)


def mul():
    if(e.get() == "Dude , Seriously !! ERROR" or e.get() == "Clear And Try Again"):
        e.delete(0, END)
        e.insert(0, "Clear And Try Again")
        return
    firstnum = e.get()
    global f_num
    global ch
    ch = '*'
    f_num = float(firstnum)
    e.delete(0, END)


def div():
    if(e.get() == "Dude , Seriously !! ERROR" or e.get() == "Clear And Try Again"):
        e.delete(0, END)
        e.insert(0, "Clear And Try Again")
        return
    firstnum = e.get()
    global f_num
    global ch
    ch = '/'
    f_num = float(firstnum)
    e.delete(0, END)


def equal():
    try:
        if(e.get() == "Dude , Seriously !! ERROR" or e.get() == "Clear And Try Again"):
            e.delete(0, END)
            e.insert(0, "Clear And Try Again")
        elif(e.get() == "Enter Your Expression"):
            e.delete(0, END)
            e.insert(0, "Enter Your Expression")
        elif(e.get() == ""):
            return
        else:
            secondnum = float(e.get())
            e.delete(0, END)
            if(ch == '+'):
                if(f_num % 1 == 0 and secondnum % 1 == 0):
                    e.insert(0, int(f_num + secondnum))
                else:
                    e.insert(0, f_num + float(secondnum))
            elif(ch == '-'):
                if(f_num % 1 == 0 and secondnum % 1 == 0):
                    e.insert(0, int(f_num) - int(secondnum))
                else:
                    e.insert(0, f_num - float(secondnum))
            elif(ch == '*'):
                if(f_num % 1 == 0 and secondnum % 1 == 0):
                    e.insert(0, int(f_num) * int(secondnum))
                else:
                    e.insert(0, f_num * float(secondnum))
            elif(ch == '/'):
                if(f_num % float(secondnum) == 0):
                    temp = int(f_num / int(secondnum))
                    e.insert(0, temp)
                else:
                    e.insert(0, f_num / float(secondnum))
            elif(ch == '='):
                e.insert(0, int(secondnum))
                return
            else:
                e.insert(0, "Clear And Try Again")
    except ZeroDivisionError:
        e.insert(0, "Dude , Seriously !! ERROR")


btn_1 = Button(root, text='1', padx=20, pady=10,
               command=lambda: addbtn(1), bg="#e8ebe9")
btn_2 = Button(root, text='2', padx=20, pady=10,
               command=lambda: addbtn(2), bg="#e8ebe9")
btn_3 = Button(root, text='3', padx=20, pady=10,
               command=lambda: addbtn(3), bg="#e8ebe9")
btn_4 = Button(root, text='4', padx=20, pady=10,
               command=lambda: addbtn(4), bg="#e8ebe9")
btn_5 = Button(root, text='5', padx=20, pady=10,
               command=lambda: addbtn(5), bg="#e8ebe9")
btn_6 = Button(root, text='6', padx=20, pady=10,
               command=lambda: addbtn(6), bg="#e8ebe9")
btn_7 = Button(root, text='7', padx=20, pady=10,
               command=lambda: addbtn(7), bg="#e8ebe9")
btn_8 = Button(root, text='8', padx=20, pady=10,
               command=lambda: addbtn(8), bg="#e8ebe9")
btn_9 = Button(root, text='9', padx=20, pady=10,
               command=lambda: addbtn(9), bg="#e8ebe9")
btn_0 = Button(root, text='0', padx=20, pady=10,
               command=lambda: addbtn(0), bg="#e8ebe9")
btn_add = Button(root, text="+", padx=19, pady=10, command=add, bg="#e8ebe9")
btn_sub = Button(root, text="-", padx=20, pady=10, command=sub, bg="#e8ebe9")
btn_mul = Button(root, text="*", padx=20, pady=10, command=mul, bg="#e8ebe9")
btn_div = Button(root, text="/", padx=20, pady=10, command=div, bg="#e8ebe9")
btn_clr = Button(root, text="Clear", padx=9, pady=10,
                 command=clear, bg="#e8ebe9")
btn_equal = Button(root, text="=", padx=19, pady=10,
                   command=equal, bg="#e8ebe9")

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)

btn_add.grid(row=4, column=3)
btn_equal.grid(row=4, column=1)
btn_sub.grid(row=4, column=2)
btn_mul.grid(row=2, column=3)
btn_div.grid(row=3, column=3)
btn_clr.grid(row=1, column=3)

root.mainloop()
