from tkinter import *


def addBtn(symbol):
    """ Adds text to the entry label."""
    presentEntry = entry.get();
    entry.delete(0, END);
    entry.insert(0, presentEntry + symbol);

root = Tk();
root.title("Calculator");

entry = Entry(root, width = 50, borderwidth = 5);
entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10);

# Number buttons
btn_1 = Button(root, text = "1", padx = 30, pady = 20, command = lambda: addBtn("1"));
btn_2 = Button(root, text = "2", padx = 30, pady = 20, command = lambda: addBtn("2"));
btn_3 = Button(root, text = "3", padx = 30, pady = 20, command = lambda: addBtn("3"));
btn_4 = Button(root, text = "4", padx = 30, pady = 20, command = lambda: addBtn("4"));
btn_5 = Button(root, text = "5", padx = 30, pady = 20, command = lambda: addBtn("5"));
btn_6 = Button(root, text = "6", padx = 30, pady = 20, command = lambda: addBtn("6"));
btn_7 = Button(root, text = "7", padx = 30, pady = 20, command = lambda: addBtn("7"));
btn_8 = Button(root, text = "8", padx = 30, pady = 20, command = lambda: addBtn("8"));
btn_9 = Button(root, text = "9", padx = 30, pady = 20, command = lambda: addBtn("9"));
btn_0 = Button(root, text = "0", padx = 30, pady = 20, command = lambda: addBtn("0"));
btn_point = Button(root, text = ".", padx = 32, pady = 20, command = lambda: addBtn("."));

# Function buttons
btn_clr = Button(root, text = "Clear", padx = 19, pady = 20, command = addBtn);
btn_add = Button(root, text = "+", padx = 29, pady = 20, command = addBtn);
btn_sub = Button(root, text = "-", padx = 31, pady = 20, command = addBtn);
btn_mul = Button(root, text = "*", padx = 30, pady = 20, command = addBtn);
btn_div = Button(root, text = "/", padx = 31, pady = 20, command = addBtn);
btn_equ = Button(root, text = "=", padx = 29, pady = 20, command = addBtn);
btn_sqrt = Button(root, text = "SQRT", padx = 19, pady = 20, command = addBtn);
btn_recp = Button(root, text = "RECP", padx = 19, pady = 20, command = addBtn);
btn_recp = Button(root, text = "RECP", padx = 19, pady = 20, command = addBtn);
btn_memstr = Button(root, text = "MS", padx = 25, pady = 20, command = addBtn);
btn_memrec = Button(root, text = "MR", padx = 24.4999, pady = 20, command = addBtn);
btn_memclr = Button(root, text = "MC", padx = 24, pady = 20, command = addBtn);
btn_memadd = Button(root, text = "M+", padx = 24, pady = 20, command = addBtn);
btn_memsub = Button(root, text = "M-", padx = 25.4999, pady = 20, command = addBtn);

# Buttons in root form
btn_1.grid(row = 1, column = 0);
btn_2.grid(row = 1, column = 1);
btn_3.grid(row = 1, column = 2);

btn_4.grid(row = 2, column = 0);
btn_5.grid(row = 2, column = 1);
btn_6.grid(row = 2, column = 2);

btn_7.grid(row = 3, column = 0);
btn_8.grid(row = 3, column = 1);
btn_9.grid(row = 3, column = 2);

btn_0.grid(row = 4, column = 0);
btn_add.grid(row = 4, column = 1);
btn_sub.grid(row = 4, column = 2);

btn_mul.grid(row = 5, column = 0);
btn_div.grid(row = 5, column = 1);
btn_equ.grid(row = 5, column = 2);

btn_clr.grid(row = 6, column = 0);
btn_sqrt.grid(row = 6, column = 1);
btn_recp.grid(row = 6, column = 2);

btn_memstr.grid(row = 1, column = 3);
btn_memrec.grid(row = 2, column = 3);
btn_memclr.grid(row = 3, column = 3);
btn_memadd.grid(row = 4, column = 3);
btn_memsub.grid(row = 5, column = 3);
btn_point.grid(row = 6, column = 3);

root.mainloop();
