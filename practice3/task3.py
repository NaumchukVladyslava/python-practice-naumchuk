print("Naumchuk Vladyslava, IT-31")

number_first = float(input("Enter a number: "))
operator = input("Enter operator: ")
number_second = float(input("Enter another number: "))

if operator == "+":
    result = number_first + number_second
    print(f"{number_first} {operator} {number_second} = {result:.4f}")
elif operator == "-":
    result = number_first - number_second
    print(f"{number_first} {operator} {number_second} = {result:.4f}")
elif operator == "*":
    result = number_first * number_second
    print(f"{number_first} {operator} {number_second} = {result:.4f}")
elif operator == "**":
    result = number_first ** number_second
    if isinstance(result, complex):
        print("Result is a complex number, cannot be displayed as a decimal")
    else:
        print(f"{number_first} {operator} {number_second} = {result:.4f}")
elif operator == "/":
    if number_second == 0:
        print("Invalid second number: division by zero")
    else:
        result = number_first / number_second
        print(f"{number_first} {operator} {number_second} = {result:.4f}")
elif operator == "//":
    if number_second == 0:
        print("Invalid second number: division by zero")
    else:
        result = number_first // number_second
        print(f"{number_first} {operator} {number_second} = {result:.4f}")
elif operator == "%":
    if number_second == 0:
        print("Invalid second number: division by zero")
    else:
        result = number_first % number_second
        print(f"{number_first} {operator} {number_second} = {result:.4f}")
else:
    print("Operator not recognised")
