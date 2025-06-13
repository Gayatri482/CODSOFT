
# Simple Calculator with Choice
def calculator():
    print("Welcome to Smart Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Choose operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print("Answer:", num1 + num2)
    elif operator == '-':
        print("Answer:", num1 - num2)
    elif operator == '*':
        print("Answer:", num1 * num2)
    elif operator == '/':
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Answer:", num1 / num2)
    else:
        print("Invalid operator!")

calculator()
