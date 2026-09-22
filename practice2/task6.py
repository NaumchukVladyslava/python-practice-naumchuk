name = input("Enter a name: ")
age = int(input("Enter an age: "))

in_range = 18 <= age <= 60
is_even = age % 2 == 0

print(f"Чи потрапляє вік у діапазон від 18 до 60 включно?: {in_range}")
print(f"Чи є вік парним числом?: {is_even}")
print(f"Чи виконуються обидві умови одночасно?: {in_range and is_even}")
print(f"Чи виконується хоча б одна з умов?: {in_range or is_even}")

print(f"До 60 років залишилося: {60 - age}")


