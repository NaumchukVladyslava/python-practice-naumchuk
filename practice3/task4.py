print("Naumchuk Vladyslava, IT-31")

grade = int(input("Enter a grade: "))

if grade < 0 or grade > 100:
    print("Error: Invalid grade!")
else:
    absences = int(input("Enter number of absences: "))

    total_lessons = 16
    max_allowed_absences = total_lessons * 0.3

    if 90 <= grade <= 100:
        text_grade = ("Excellent grade")
    elif 82 <= grade <= 89:
        text_grade = ("Good grade")
    elif 74 <= grade <= 81:
        text_grade = ("Good grade")
    elif 64 <= grade <= 73:
        text_grade = ("Satisfactory grade")
    elif 60 <= grade <= 63:
        text_grade = ("Satisfactory grade")
    elif 0 <= grade <= 59:
        text_grade = ("Unsatisfactory grade")

    if absences > max_allowed_absences:
        print("Not allowed")

    if absences > max_allowed_absences or grade <= 59:
        status = "failed"
    else:
        status = "passed"

    print(f"Grade: {grade}, Result: {text_grade}, Status: {status}")
