print("Naumchuk Vladyslava, IT-31")

day = int(input("Enter a day: "))
month = input("Enter a month: ")
year = int(input("Enter a year: "))

is_valid = True

if (month == "January" or month == "1" or
    month == "February" or month == "2" or
    month == "March" or month == "3" or
    month == "April" or month == "4" or
    month == "May" or month == "5" or
    month == "June" or month == "6" or
    month == "July" or month == "7" or
    month == "August" or month == "8" or
    month == "October" or month == "9" or
    month == "October" or month == "10" or
    month == "November" or month == "11" or
    month == "December" or month == "12"):
    print(f"Month:{month}")
else:
    print("Month is invalid. Month must be between 1 and 12")
    is_valid = False

if (month == "January" or month == "1" or
    month == "March" or month == "3"  or
    month == "May" or month == "5" or
    month == "July" or month == "7" or
    month == "August" or month == "8" or
    month == "October" or month == "10" or
    month == "December" or month == "12"):
    if day >= 1 and day <= 31:
        print(f"Day:{day}")
    else:
        print(f"Day is invalid. Day must be between 1 and 31.")
        is_valid = False

elif month == "April" or month == "4" or month == "June" == "6" or month == "September" == "9" or month == "November" == "11":
    if day > 1 and day < 30:
            print(f"Day:{day}")
    else:
        print(f"Day is invalid. Day must be between 1 and 30.")
        is_valid = False

elif month == "February" or month == "2":
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if day >= 1 and day <= 29:
            print(f"Day:{day}")
        else:
            print(f"Day is invalid. Day must be between 1 and 29.")
            is_valid = False
    else:
        if day >= 1 and day <= 28:
            print(f"Day:{day}")
        else:
            print(f"Day is invalid. Day must be between 1 and 28.")
            is_valid = False
else:
    print("Month is invalid. Month name is incorrect.")
    is_valid = False

if year > 0:
    print(f"Year:{year}")
else:
    print("Year is invalid. Year must be positive.")
    is_valid = False

if is_valid:
    print("Date is valid")
else:
    print("Date is invalid")
