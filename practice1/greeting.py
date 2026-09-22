# Program: Personalized Greeting
name = "Vladyslava"
surname = "Naumchuk"
group = "IT-31"
birth_year = 2009
current_year = 2026

age = current_year - birth_year
full_name = name + " " + surname

print(f"Welcome, {name} !")
print("Full Name:", full_name)
print("Age:", age)
print("Group:", group)
print("\n")
print("Number of letters in the full name:", len(full_name))
print("Loud version:", full_name.upper())
