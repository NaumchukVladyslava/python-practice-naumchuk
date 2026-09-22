print("Naumchuk Vladyslava, IT-31")

group = "IT-31"
d = 24
m = 2
y = 2009

number = int(input("Enter a number:"))
number = abs(number)

counter = 0
sum = 0
new_number = 0

max_digit = -1
min_digit = 10

while number > 0:
    counter +=1

    digit = number % 10

    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit

    suma = sum + digit

    new_number = new_number * 10 + digit
    number = number // 10

print(f"Digits: {counter}")
print(f"Sum of digits: {sum}")
print(f"Max digit: {max_digit}, min digit: {min_digit}")
print(f"Reversed: {new_number}")



