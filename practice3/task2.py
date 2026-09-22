print("Naumchuk Vladyslava, IT-31")

number = int(input("Enter a number:"))

if number > 0:
    print("You number is positive")
    if number % 2 == 0:
        print("You number is even")
elif number < 0:
    print("You number is negative")
    if number % 2 == 0:
        print("You number is even")
elif number == 0:
    print("You number zero")
