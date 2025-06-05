from datetime import date

num = int(input('What year do you want to analyze? Enter 0 to analyze the current year: '))

if num % 4 == 0 and (num % 100 != 0 or num % 400 == 0):
    print("It's a leap year")
else:
    print("It's not a leap year")