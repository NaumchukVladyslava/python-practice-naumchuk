print("Naumchuk Vladyslava, IT-31")

group = "IT-31"
d = 24
c = 10

counter = 0
sum = 0
product = 1
parity_count = 0
not_parity_count = 0

for i in range(d, 32):
    print(i, end=" ")

    counter += 1
    sum += i
    product *= i

    average_arithmetic = sum / counter

    if i % 2 == 0:
        parity_count += 1
    else:
        not_parity_count += 1

print()
print(f"К-сть чисел вивелося: {counter}")
print(f"Сума: {sum}")
print(f"Добуток: {product}")
print(f"Середнє арифметичне: {average_arithmetic}")
print(f"Парних чисел: {parity_count}")
print(f"Непарних чисел: {not_parity_count}")

# while version

count = d

counter = 0
sum = 0
product = 1
parity_count = 0
not_parity_count = 0

while count <= 31:
    print(count, end=" ")

    counter += 1
    sum += count
    product *= count

    if count % 2 == 0:
        parity_count += 1
    else:
        not_parity_count += 1

    count += 1

average_arithmetic = sum / counter

print()
print(f"К-сть чисел вивелося: {counter}")
print(f"Сума: {sum}")
print(f"Добуток: {product}")
print(f"Середнє арифметичне: {average_arithmetic}")
print(f"Парних чисел: {parity_count}")
print(f"Непарних чисел: {not_parity_count}")

print()
print(f"Зворотній відлік")
for i in range(c, 0, -1):
    print(i, end=" ")
