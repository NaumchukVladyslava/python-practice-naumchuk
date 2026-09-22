print("Naumchuk Vladyslava, IT-31")

grade = int(input("Enter a grade (0-100) :"))

counter = 1

while grade < 0 or grade > 100:
    if grade > 100:
        print("Grade must be more 100")

    if grade < 0:
        print("Grade must be less than 0")

    grade = int(input("Enter a grade (0-100): "))
    counter += 1

if 90 <= grade <= 100:
    text_grade = ("A")
elif 82 <= grade <= 89:
    text_grade = ("B")
elif 74 <= grade <= 81:
    text_grade = ("C")
elif 64 <= grade <= 73:
    text_grade = ("D")
elif 60 <= grade <= 63:
    text_grade = ("E")
elif 0 <= grade <= 59:
    text_grade = ("F")

print(f"Grade: {grade}")
print(f"Accepted after: {counter} attempts")
print(f"Grade: {text_grade}")
