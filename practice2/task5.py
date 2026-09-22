a = 24
b = 2

additivity = 0
parity = 2

print(additivity < a)
print(a % parity == 0)
print(additivity < a and a % parity == 0)

product = a * b

print(additivity < product)
print(product % parity == 0)
print(additivity < product and product % parity == 0)


