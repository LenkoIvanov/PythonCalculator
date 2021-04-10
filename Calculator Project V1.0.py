import math
import os

global MEMORYRESULT; #global variable for memory functions (they can be called at the start)
MEMORYRESULT = None;

def printMenu(): 
    print("Type in the symbol of the action, you wish to perform: ");
    print(" '+'-addition         '-'-subtraction \n" +
          " '*'-multiplication   '/'- division    \n" +
          " 'SQRT'- square root  'RECP'- reciprocal \n" +
          " 'MS'- memory store   'MC'- memory clear \n" +
          " 'MR'- memory remind  'M-'- memory subtract \n"+
          " 'M+'- memory add     'C'- clear all \n"+
          " 'x' or 'X'- exit ");

def numconversion(a):
    if('.' in a):     #if number contains a '.' - it's a floating point
        return float(a);
    else:
        return int(a);

def numInput():
    ina = None;
    outa = None;
    while True:  #if user enters something different from a number, user is prompted again
        try:
            ina = input("Enter a number: " );
            outa = numconversion(ina);
            break;
        except:
            print("Fatal error! You can enter only numbers!");
    return outa;

def addition():
    a = numInput();
    b = numInput();
    result = a + b;
    return result;
    
def subtraction():
    a = numInput();
    b = numInput();
    result = a - b;
    return result;

def multiplication():
    a = numInput();
    b = numInput();
    result = a * b;
    return result;

def division():
    a = numInput();
    b = None;
    while True:
        b = numInput();
        if b == 0:
            print("Fatal error! Division by zero impossible!");
        else:
            break;
    result = a / b;
    return result;

def squareRoot():
    while True:
        num = numInput();
        if(num >= 0):
            break;
        else:
            print("Fatal error! There is no real definition of a negative square root!") 
    result = math.sqrt(num);
    return result;
    
def reciprocal():
    while True:
        num = numInput();
        if(num != 0):
            break;
        else:
            print("Fatal error! Division by zero impossible!")
    result = 1 / num;
    return result;

def memoryStore(result):
    global MEMORYRESULT;
    MEMORYRESULT = result;

def memoryClear():
    global MEMORYRESULT;
    MEMORYRESULT = None;
    
def memoryRecall():
    print("Current result in memory: " + str(MEMORYRESULT));

def memoryAdd(result):
    global MEMORYRESULT;
    if (MEMORYRESULT != None):  #these functions can be called at the start
        MEMORYRESULT += result;
    else:
        print("Fatal error! Memory is empty! Add to it and retry!");
    
def memorySubtract(result):
    global MEMORYRESULT;
    if (MEMORYRESULT != None):
        MEMORYRESULT -= result;
    else:
        print("Fatal error! Memory is empty! Add to it and retry!");

def clearCalc():   #doesn't work in IDLE
    if os.name == 'nt':   #for Windows
       os.system('cls');
    else:
        os.system('clear');  #for Linux
       
printMenu();
userinput = input("Enter: ");
result = None;

while(True):
    if(userinput == '+'):
      result = addition();
      print("Result: " + str(result));
      
    elif(userinput == '-'):
      result = subtraction();
      print("Result: " + str(result));
      
    elif(userinput == '*'):
      result = multiplication();
      print("Result: " + str(result));
      
    elif(userinput == '/'):
      result = division();
      print("Result: " + str(result));
      
    elif(userinput == 'SQRT'):
      result = squareRoot();
      print("Result: " + str(result));
      
    elif(userinput == 'RECP'):
      result = reciprocal();
      print("Result: " + str(result));
      
    elif(userinput == 'MS'):
        memoryStore(result);
        
    elif(userinput == 'MR'):
        memoryRecall();
        
    elif(userinput == 'MC'):
        memoryClear();
        
    elif(userinput == 'M+'):
        memoryAdd(result);
        memoryRecall();
        
    elif(userinput == 'M-'):
        memorySubtract(result);
        memoryRecall();

    elif(userinput == 'C'):
        clearCalc();
        memoryClear();
        result = None;
        printMenu();
        
    elif(userinput == 'x' or userinput == 'X'):
        exit();
        
    else:
        print("Wrong input. Try again!");
    userinput = input("Enter another action: ");

