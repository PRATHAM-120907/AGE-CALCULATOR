from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

while True:
    user_input = input("(YES/NO) yes for continue no for exit the program = ")
    if user_input.lower() != "yes":
        print("CLOSING THE PROGRAM...")
        break

    dob_input = input("ENTER YOUR DATE OF BIRTH IN (YYYY-MM-DD): ")
    birth_date = datetime.strptime(dob_input, "%Y-%m-%d")

    age = calculate_age(birth_date)
    print(f"YOU ARE {age} YEARS OLD")
