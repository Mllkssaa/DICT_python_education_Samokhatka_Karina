import math

from numpy.random.mtrand import choice

print("Enter the loan principal:\n>")
principal = int(input())

print("What do you want to calculate?")
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:>\n ')
choice = input()

if choice == "m":
    print("Enter the monthly payment:>\n")
    monthly_payment = int(input())
    months = principal // monthly_payment
    if principal // monthly_payment !=0:
        months += 1

    print(f"It will take {months} month{'s' if months > 1 else ''} to repay the loan")


elif choice == "p":
    print("Enter the number of months:")
    months = int(input())
    payment = principal // months
    if principal % months !=0:
        last_payment = principal - (months - 1) * (payment + 1)
        print(f"Your monthly payment = {payment + 1} and the last payment = {last_payment}.")
    else:
        print(f"Your monthly payment = {payment} ")
