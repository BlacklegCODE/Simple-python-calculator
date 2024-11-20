#simple python calculator


a = int(input("Enter first digit :"))
b = int(input("Enter second digit :"))
c = input("Enter the operand :")

while not c == "x":

    if c == "-":
        d = a-b
        print(f"The subtraction is :{d}")

    elif c == "+":
        d = a+b
        print(f"The addition is :{d}")

    elif c == "*":
        d = a*b
        print(f"The subtraction is :{d}")

    elif c == "/":
        d = a/b
        print(f"The subtraction is :{d}")

    else :
        print("Enter a valid operand !")

    c = input("Enter the operand :")
