birthYear = None
while birthYear == None or (2025-birthYear) >= 150:
    try:
        birthYear = int(input("What's your birth year?"))
    except ValueError:
        print("Please enter a valid number.")

print((2025-birthYear))