print("Naumchuk Vladyslava, IT-31")

d = 24
c = 10
n = d * c

print(f"n = {d} * {c} = {n}")

#1
counter = 0
suma = 0
i = 1

print("Divisors: ", end="")
while i <= n:
    if n % i == 0:
        print(i, end=" ")
        counter += 1
        suma += i
    i += 1

print()
print(f"Divisors count: {counter}, sum: {suma}")

#2
divisor_check = 2
is_prime = True

while divisor_check < n:
    if n % divisor_check == 0:
        is_prime = False
        break
    divisor_check += 1
else:
    is_prime = True

if is_prime and n > 1:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

#3
prime_counter = 0
current_number = 2

print(f"Primes up to {n}: ", end="")
while current_number <= n:
    divisor = 2
    current_is_prime = True

    while divisor < current_number:
        if current_number % divisor == 0:
            current_is_prime = False
            break
        divisor += 1

    if current_is_prime:
        print(current_number, end=" ")
        prime_counter += 1

    current_number += 1

print()
print(f"Primes count: {prime_counter}")
