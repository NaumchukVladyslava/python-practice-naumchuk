print("Naumchuk Vladyslava, IT-31")
name = input("What is your name? ")
age = int(input("What is your age? "))

if not name:
    print("Invalid name")
    name = "Anonymous"

if age < 0:
    category = "Некоректне значення"
elif 0 <= age <= 6:
    category = "child"
elif 7 <= age <= 17:
    category = "schoolchild"
elif 18 <= age <= 64:
    category = "adult"
elif age >= 65:
    category = "senior"

print(f"Welcome, {name}! You are in category {category}.")
