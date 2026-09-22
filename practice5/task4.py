print("Naumchuk Vladyslava, IT-31")

name = "Vlada"
group = "IT-31"
n = len(name)

#1
def read_grade(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            grade = int(user_input)
            if 0 <= grade <= 100:
                return grade
            print("Error: the value must be between 0 and 100")
        else:
            print("Error: digits only")

#2
def to_letter(grade):
    if 90 <= grade <= 100:
        return "A"
    if 82 <= grade <= 89:
        return "B"
    if 74 <= grade <= 81:
        return "C"
    if 64 <= grade <= 73:
        return "D"
    if 60 <= grade <= 63:
        return "E"
    return "F"

#3
def average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades) if grades else 0.0

#4
def count_above(grades, limit):
    count_limit = 0
    for grade in grades:
        if grade > limit:
            count_limit += 1
    return count_limit

#5
def print_report(name, group, grades):
    avg = average(grades)
    letter = to_letter(avg)
    above = count_above(grades, avg)
    grades_str = " ".join(str(g) for g in grades)

    print("\n-Report-")
    print(f"Student: {name}, group {group}")
    print(f"Grades: {grades_str}")
    print(f"Average: {avg:.2f} -> {letter}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {above}")

#6
def main():
    name = "Vlada"
    group = "IT-31"
    n = len(name)

    grades = [80, 95, 85, 90, 90]

    print_report(name, group, grades)

#7
main()