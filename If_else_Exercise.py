"""
#1.Write a Python program to check if a number is positive.

while True:
    try:
        number = int(input("Enter the number: "))
        if number > 0:
            print(f"{number} is a positive number.")
        elif number==0:
            print("the number is Zero")
        else:
            print(f"{number} is a negetive number.")

    except ValueError:
        print("Invalid entry! Please enter a number.")

#2.Print "Eligible to vote" if age is 18 or above.
while True:
    age = float(input("Enter your Age."))
    if age >= 18:
        print(f"Welcome, you can vote.")
    elif age < 18:
        print(f"Your are not eligible to vote.")
    else:
        print(f"you are a ghost.")

#3.Check if a number is divisible by 7.
while True:
    num = int(input("\nPlease Enter a Number."))
    if num % 7 == 0:
        print(f"Yes,{num}can devid by 7.")
    else:
        print(f"Not devidable by 7.")
        

#4.Print "Pass" if marks are greater than 40.
while True:
    try:
        marks = float(input(f"please enter your Marks."))
        if marks >= 40:
            print(f"PASS")
        else:
            print(f"Fail")
    except ValueError:
        print("Invalid Input: Please enter numbers only.")

#5.Check if a number is greater than 100.
while True:
    try:
        number = int(input("Please enter the number"))
        if number > 100:
            print (f"Yes,{number} the number is greater then 100")
        elif number ==100:
            print(f"this is equal to 100")
        else:
            print(f"No,{number} Number is smaller than 100")
    except ValueError:
        print ("invalid input:Please enter the num only")

ProgrammingQuestion.py

while True:
    try:
        temprature = int(input(f" what is the temprature today"))
        if temprature >= 45:
            print(f" Alert, the temprature is exceeding")
        else:
            print(f"Current temperature: {current_temp}°C. Status: Safe.")
    except ValueError:
        print("Invalid input: Please enter the number only.")

#7.Check if a string length is more than 8 characters.

while True:
        str = (input(f"Please Enter the string "))
        if len(str)>8:
            print(f"Yes, String lenght is going beyong 8:,{len(str)}")
        else:
            print("No, the string is not more than 8")
"""
#Print "Logged In" if password matches "admin123".
while True:
    login = input("Please Enter the password")
    if login == 'admin123':
        print("Welcome, you have logged in successfully")
        Break
    else:
        print ("Please enter a valid password")
