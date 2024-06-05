#Question 8
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Enter + for Addition, - for subtraction, * for multiplication and / for division")
operation=str(input())
if operation=="+":
    print(num1+num2)
if operation=="-":
    print(num1-num2)
if operation=="*":
    print(num1*num2)
if operation=="/":
    print(num1/num2)
