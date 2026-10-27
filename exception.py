# try:
#     number=int(input("Enter the number: "))
#     print(1/number)

# except ZeroDivisionError:
#     print("not divisible by 0")

# except ValueError:
#     print("enter only numbers")

# except Exception:
#     print("something went wrong")

# finally:
#     print("do some cleanup")   

# try:
#     print("hello"
#     except SyntaxError:
#     print("there is a syntax error")

# try:
#     exec('print("hello")')  
# except SyntaxError:
#     print("error,there is a syntax error")

# try:
#     print(total)
# except NameError:
#     print("the variable is not defiened")

# try:
#     print(1+"1")
# except TypeError:
#     print("string and integer cannot be conacatenated") 

# try:
#     numbers=[1,2,3,4,5]
#     print(number[10])
# except NameError:
#     print("error,there is no given value for the given index")    

# try:
#     student={"name":"salih"}
#     print(student["age"])
# except KeyError:
#     print("enter the correct key value")

# try:
#     open("filess.txt","r")
# except FileNotFoundError:
#     print("file is not found")    

# try:
#     import maths
# except ModuleNotFoundError:
#     print("no module present")

# try:
#     from math import squareroot
# except ImportError:
#     print("there is an import error in the function does not exist")

try:
    number=10
    print(number.append(8))
except AttributeError:
    print("attribute error,the append function does not exist for integers")



def withdraw(balance,amount):
    if amount>balance:
        raise RuntimeError("insufficient balance")
    return balance-amaount
try:
    withdraw(500,1000)
except RuntimeError as e :
    print(e)

    
        
        