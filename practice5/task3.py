print("Naumchuk Vladyslava, IT-31")

name = "Vladyslava"
surname = "Naumchuk"
c = len(surname)


#1
def get_initials(name: str, surname: str) -> str:
    return f"{name[0]}.{surname[0]}."

print(f"{name} {surname}")
result = get_initials(name, surname)
print(f"Initials: {result}")


#2
def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    return text.lower().count(letter.lower())

print(f"Letters in surname: {c}")


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

vowel_letters = count_vowels(surname)
consonant_letters = c - vowel_letters
print(f"Vowels: {vowel_letters}, consonants: {consonant_letters}")


#3
for v in "aeiou":
    print(f"{v}: {count_letters(text=surname, letter=v)}")


#4
default_count = count_letters(surname)
print(f"Default letter 'a': {default_count}")


#5
def reverse_text(text: str) -> str:
    reversed_str = ""
    for char in text:
        reversed_str = char + reversed_str
    return reversed_str

print(f"Reversed surname: {reverse_text(surname)}")


#6
print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")