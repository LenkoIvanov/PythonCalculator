from tkinter import *
from tkinter import messagebox
import math

def numconversion(a):
    """ Converts the numbers entered by the user"""
    if('.' in a):
        return float(a)
    else:
        return int(a)
    
def addBtn(symbol):
    """ Used to type in numbers in the label"""
    presentEntry = entry.get()
    entry.delete(0, END)
    entry.insert(0, presentEntry + symbol)

def btnClear():
    """ Clears all global variables and empties memory"""
    entry.delete(0, END)
    global char
    char = None
    global first
    first = None
    global result
    result = None

def btnCE():
    """ Clears current entry only """
    entry.delete(0, END)
    global first
    first = None
    global char
    char = None
    
def addSign(a):
    """ Converts negative into positive and positive into negative """
    if a > 0:
        x = -abs(a)
        return x
    elif a < 0:
        x = abs(a)
        return x
    
def btnSign():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    signedNum = addSign(first)
    entry.insert(0, signedNum)

def Add():
    """ Passes two global variables to the equal method, similiar for -,*,/,**"""
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    global char
    char = "+"
    
def Sub():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    global char
    char = "-"

def Mul():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    global char
    char = "*"

def Div():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    global char
    char = "/"
    
def Pow():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    global char
    char = "**"

def Mod():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    global char
    char = "mod"
    
def Equal():
    """Where the calculations for two operand methods take place"""
    b = entry.get()
    second = numconversion(b)
    # TODO find a way to make the second negative as well, same for rad and grad
    entry.delete(0, END)
    if (char == "+"):
        result = first + second
        entry.insert(0, result)  
    elif(char == "-"):
        result = first - second
        entry.insert(0, result)
    elif(char == "*"):
        result = first * second
        entry.insert(0, result)
    elif(char == "/"):
        if(second != 0):
            result = first/second
            entry.insert(0, result)
        else:
            messagebox.showerror("Error", "Division by zero is impossible!")
    elif(char == "**"):
        result = first ** second
        entry.insert(0, result)
    elif(char == "mod"):
        result = math.fmod(first, second)
        entry.insert(0, result)

def Log():
    """ Similar functions for all one operand methods"""
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    if(first > 0):
        result = math.log(first)
        entry.insert(0, result)
    else:
        messagebox.showerror("Error", "No log for non-positive integers!")
    
def Recp():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    if(first != 0):
        result = 1 / first
        entry.insert(0, result)
    else:
        messagebox.showerror("Error", "Division by zero is impossible!")
    
def Sqrt():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    if first >= 0:
        result = math.sqrt(first)
    else:
        messagebox.showerror("Error", "No square root for negatives!")
    entry.insert(0, result)
    
def SqPw():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    result = first ** 2
    entry.insert(0, result)
    
def Fact(): #TODO fix factorial calculations
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    if(first <= 0 or ('.' in str(first))):
        messagebox.showerror("Error", "Factorial only for non-negative integers!")
    elif(first == 0):
        result = 1
        entry.insert(0, result)
    else:
        result = 1
        for i in range(first):
            result *= i
        entry.insert(0, result)

def tenPow():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    result = 10 ** first
    entry.insert(0, result)
    
def Exp():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    result = math.exp(first)
    entry.insert(0, result)
    
def sin():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    result = math.sin(first)
    entry.insert(0, result)
    
def cos():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    result = math.cos(first)
    entry.insert(0, result)
    
def tan():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    result = math.tan(first)
    entry.insert(0, result)
    
def radConv():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    converted = math.radians(first)
    entry.insert(0, converted)
    
def degConv():
    a = entry.get()
    global first
    first = numconversion(a)
    entry.delete(0, END)
    converted = math.degrees(first)
    entry.insert(0, converted)

def memoryStore():
    global result
    result = entry.get()
    
def memoryRecall():
    global result
    if (result != None):
        entry.insert(0, result)
    else:
        messagebox.showerror("Error", "Memory is empty!")
        
def memoryAdd():
    global result
    if (result != None):
        presentRes = entry.get()
        result = result + presentRes
    else:
        messagebox.showerror("Error", "Memory is empty!")
        
def memorySub(): #TODO fix weird error
    global result
    if (result != None):
        presentRes = entry.get()
        result = result - presentRes
    else:
        messagebox.showerror("Error", "Memory is empty!")
        
def memoryClear():
    global result
    result = None


root = Tk()
root.title("Scientific Calculator")

entry = Entry(root, width = 50, borderwidth = 5)
entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
entry.bind("<Key>", lambda e: "break") #disable keyboard input

# Number buttons
btn_1 = Button(root, text = "1", padx = 41, pady = 20, command = lambda: addBtn("1"))
btn_2 = Button(root, text = "2", padx = 41, pady = 20, command = lambda: addBtn("2"))
btn_3 = Button(root, text = "3", padx = 41, pady = 20, command = lambda: addBtn("3"))
btn_4 = Button(root, text = "4", padx = 41, pady = 20, command = lambda: addBtn("4"))
btn_5 = Button(root, text = "5", padx = 41, pady = 20, command = lambda: addBtn("5"))
btn_6 = Button(root, text = "6", padx = 41, pady = 20, command = lambda: addBtn("6"))
btn_7 = Button(root, text = "7", padx = 41, pady = 20, command = lambda: addBtn("7"))
btn_8 = Button(root, text = "8", padx = 41, pady = 20, command = lambda: addBtn("8"))
btn_9 = Button(root, text = "9", padx = 41, pady = 20, command = lambda: addBtn("9"))
btn_0 = Button(root, text = "0", padx = 41, pady = 20, command = lambda: addBtn("0"))
btn_point = Button(root, text = ".", padx = 41, pady = 20, command = lambda: addBtn("."))


# Function buttons
btn_pi = Button(root, text = "Pi", padx = 38, pady = 20, command = addBtn)
btn_sign = Button(root, text = "+/-", padx = 34, pady = 20, command = btnSign)
btn_clr = Button(root, text = "Clear", padx = 30, pady = 20, command = btnClear)
btn_clrent = Button(root, text = "CE", padx = 36, pady = 20, command = btnCE)
btn_add = Button(root, text = "+", padx = 39, pady = 20, command = Add)
btn_sub = Button(root, text = "-", padx = 40, pady = 20, command = Sub)
btn_mul = Button(root, text = "*", padx = 40, pady = 20, command = Mul)
btn_div = Button(root, text = "/", padx = 40, pady = 20, command = Div)
btn_equ = Button(root, text = "=", padx = 39, pady = 20, command = Equal)
btn_sqrt = Button(root, text = "SQRT", padx = 30, pady = 20, command = Sqrt)
btn_log = Button(root, text = "log", padx = 35, pady = 20, command = Log)
btn_recp = Button(root, text = "RECP", padx = 40, pady = 20, command = Recp)
btn_sqpw = Button(root, text = "x^2", padx = 34, pady = 20, command = SqPw)
btn_pow = Button(root, text = "x^y", padx = 34, pady = 20, command = Pow)
btn_mod = Button(root, text = "Mod", padx = 30, pady = 20, command = Mod)
btn_tenpow = Button(root, text = "10^x", padx = 30, pady = 20, command = tenPow)
btn_fact = Button(root, text = "n!", padx = 38, pady = 20, command = Fact)
btn_exp = Button(root, text = "Exp", padx = 35, pady = 20, command = Exp)
btn_sin = Button(root, text = "sin", padx = 36, pady = 20, command = sin)
btn_cos = Button(root, text = "cos", padx = 35, pady = 20, command = cos)
btn_tan = Button(root, text = "tan", padx = 35, pady = 20, command = tan)
btn_rad = Button(root, text = "RAD", padx = 33, pady = 20, command = radConv)
btn_deg = Button(root, text = "DEG", padx = 32, pady = 20, command = degConv)

# Memory buttons
btn_memstr = Button(root, text = "MS", padx = 35, pady = 20, command = memoryStore)
btn_memrec = Button(root, text = "MR", padx = 34.4999, pady = 20, command = memoryRecall)
btn_memclr = Button(root, text = "MC", padx = 34, pady = 20, command = memoryClear)
btn_memadd = Button(root, text = "M+", padx = 34, pady = 20, command = memoryAdd)
btn_memsub = Button(root, text = "M-", padx = 35.4999, pady = 20, command = memorySub)

# Buttons in root form
btn_memstr.grid(row = 1, column = 0)
btn_memrec.grid(row = 1, column = 1)
btn_memclr.grid(row = 1, column = 2)
btn_memadd.grid(row = 1, column = 3)
btn_memsub.grid(row = 1, column = 4)

btn_sqpw.grid(row = 2, column = 0)
btn_pow.grid(row = 2, column = 1)
btn_sin.grid(row = 2, column = 2)
btn_cos.grid(row = 2, column = 3)
btn_tan.grid(row = 2, column = 4)

btn_sqrt.grid(row = 3, column = 0)
btn_tenpow.grid(row = 3, column = 1)
btn_log.grid(row = 3, column = 2)
btn_exp.grid(row = 3, column = 3)
btn_mod.grid(row = 3, column = 4)

btn_clrent.grid(row = 4, column = 1)
btn_clr.grid(row = 4, column = 2)
btn_div.grid(row = 4, column = 4)

btn_pi.grid(row = 5, column = 0)
btn_7.grid(row = 5, column = 1)
btn_8.grid(row = 5, column = 2)
btn_9.grid(row = 5, column = 3)
btn_mul.grid(row = 5, column = 4)

btn_fact.grid(row = 6, column = 0)
btn_4.grid(row = 6, column = 1)
btn_5.grid(row = 6, column = 2)
btn_6.grid(row = 6, column = 3)
btn_sub.grid(row = 6, column = 4)

btn_sign.grid(row = 7, column = 0)
btn_1.grid(row = 7, column = 1)
btn_2.grid(row = 7, column = 2)
btn_3.grid(row = 7, column = 3)
btn_add.grid(row = 7, column = 4)

btn_deg.grid(row = 8, column = 0)
btn_rad.grid(row = 8, column = 1)
btn_0.grid(row = 8, column = 2)
btn_point.grid(row = 8, column = 3)
btn_equ.grid(row = 8, column = 4)

root.mainloop()
