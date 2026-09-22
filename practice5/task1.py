print("Naumchuk Vladyslava, IT-31")

name = "Vladyslava"
surname = "Naumchuk"
group = "IT-31"
y = 2009

#1
def print_card():
    print(f"Name: {name} {surname}\nGroup: {group}\nBirth year: {y}")

print()
print_card()
print_card()
print_card()

#2
def print_card_args(name, surname, group, y):
    print(f"Name: {name} {surname}\nGroup: {group}\nBirth year: {y}")

print()
print_card_args("Vladyslava", "Naumchuk", "IT-31", 2009)
print_card_args(y=2009, group="IT-31", surname="Naumchuk", name="Vladyslava")
print_card_args("Vladyslava", "Naumchuk", group="IT-31", y=2009)

#3
def print_card_args(name, surname, group="IT-31", y=2009):
    print(f"Name: {name} {surname}\nGroup: {group}\nBirth year: {y}")

print()
print_card_args("Vladyslava", "Naumchuk")

#4
#print_card_args("Ivan")
# Traceback (most recent call last):
#   File "/home/vlllllladas/Desktop/python-course/Practical011/task1.py", line 31, in <module>
#     print_card_args("Ivan")
# TypeError: print_card_args() missing 1 required positional argument: 'surname'
# Недостатня к-сть аргументів

#5
# print_card_args(name="Ivan", "Petrenko")
# Запуск, параметри зі значеннями за замовчуванням стоять після звичайних