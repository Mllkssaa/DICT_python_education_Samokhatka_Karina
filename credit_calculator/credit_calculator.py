import math

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number")

def get_init(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid integer")

print("What do you want to calculate?")
print('type "n" - for number of monthly payments,')
print('type "a" - for annuity monthly payment,')
print('type "p" - for loan principal,')
print('type "d" for differentiated payments \n')

choice = input("> ").lower()

if choice == "n":
    principal = get_float("Enter the loan principal:\n ")
    payment = get_float("Enter the monthly payment:\n ")
    interest = get_float("Enter the loan interest (%):\n ")

    i = interest / (12 * 100)

    denominator = payment - i * principal
    if denominator <= 0:
        print("The payment is too low to cover the interest. Loan can't be repaid")
    else:
        n = math.ceil(math.log(payment / denominator, 1 + i))

    years = n // 12
    months = n % 12

    result = "It will take"

    if years == 0:
       result += f"{years} year{'s' if years > 1 else ''}"
    elif months == 0:
        if years > 0:
            result += " and "
        result += f"{months} month{'s' if months > 1 else ''}"
    result += " to repay this loan!"
    print(result)

elif choice == "a":
    principal = get_float("Enter yhe loan principal: \n> ")
    periods = get_init("Enter the number of periods:\n> ")
    interest = get_float("Enter the loan interest (%):\n> ")

    i = interest / (12 * 100)
    annuity = principal * i * (1 + i) ** periods / ((1 + i) ** periods - 1)
    annuity = math.ceil(annuity)

    print(f"Your annuity payment = {annuity}!")

elif choice == "p":
    annuity = get_float("Enter the annuity payment:\n> ")
    periods = get_init("Enter the number of periods:\n> ")
    interest = get_float("Enter the loan interest (%):\n> ")

    print(f"Your loan principal = {principal}")

elif choice == "d":
    principal = get_float("Enter the loan principal:\n> ")
    periods = get_init("Enter the number of periods:\n> ")
    interest = get_float("Enter the loan interest (%):\n> ")

    i = interest / (12 * 100)
    total_payment = 0

    for m in range(1, periods + 1):
        d = math.ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
        total_payment += d
        print(f"Month {m}: payment is {d}")