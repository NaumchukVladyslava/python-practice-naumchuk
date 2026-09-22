print("Naumchuk Vladyslava, IT-31")

birth_year = 2009
current_year = 2026

#1
def print_age(birth_year):
    age = 2026 - birth_year
    print(age)

def get_age(birth_year, current_year = 2026):
    #6
    if birth_year > current_year or birth_year < 0:
        return -1
    age = current_year - birth_year
    return age
#6
print(get_age(3000, current_year))

#7
#print("after return")
#Тому що вже спрацював return

#2
print_age(birth_year)
get_age(birth_year, current_year = 2026)

print(print_age(birth_year))
#Функція print_age не має return, вона повертає None, який потім друкує зовнішній print

#3
age_month = get_age(birth_year, current_year) * 12
print(age_month)

age_week = get_age(birth_year, current_year) * 52
print(age_week)

#4
age_in_2030 = get_age(birth_year, current_year=2030)
print(age_in_2030)

#5
# print_age(birth_year) * 12
# Traceback (most recent call last):
#   File "/home/vlllllladas/Desktop/python-course/Practical011/task2.py", line 32, in <module>
#     print_age(birth_year) * 12
#     ~~~~~~~~~~~~~~~~~~~~~~^~~~
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'


