def calculate(a,b,op):
    if op == "+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    else:
        raise ValueError("invaid operator")

try:
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    op=input("input the operator (+ - * /) : ")
    print(f"result of {a} {op} {b} = {calculate(a,b,op)}")

except ZeroDivisionError:
    print("number cannot be divided by zero")
except ValueError as e :
    print("error",e)
finally:
    print("calculated")
    
    
