num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))

try:
    print(num1/num2)
except ZeroDivisionError:
    print("Denominator cannot be zero")
    
