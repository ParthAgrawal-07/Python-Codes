num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
opp = input("Enter the operator:")

if opp =="+" :
    print(num1+num2)
elif opp == "-" :
    print(num1-num2)
elif opp == "*" :
    print(num1*num2)
elif opp == "/" :
    print(num1/num2)
elif opp == "%" :
    print(num1%num2)
else:
    print("Invalid operator")