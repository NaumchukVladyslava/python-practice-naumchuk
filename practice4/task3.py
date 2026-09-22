print("Naumchuk Vladyslava, IT-31")

name = "Vladyslava"
surname = "Naumchuk"

vowel = 0
consonants = 0

for i in name + surname:
    if i in "aeiouAEIO":
        vowel += 1
    else:
        consonants += 1

print(name, surname)
total_letters = vowel + consonants
print(f"Vowels: {vowel}")
print(f"Consonants: {consonants}")
print(f"Total letters: {total_letters}")
