import math
import argparse
import sys

parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment: annuity or diff")
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=float)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if args.interest is None:
    print("Incorrect parameters")
    sys.exit()

def all_positive(*values):
    return all (v is None or v >= 0 for v in values)

if not all_positive(args.payment, args.principal, args.periods, args.interest):
    print("Incorrect parameters")
    sys.exit()

i = args.interest / (12 * 100)

if args.type == "diff":
    if args.payment is not None or args.principal is None or args.periods is None:
        print('Incorrect parameters')
        sys.exit()

    total_payment = 0
    for m in range(1, args.periods + 1):
        d = math.ceil(args.principal / args.periods + i * (args.principal - (args.principal * (m - 1)) / args.periods))
        total_payment += d
        print(f"Month {m}: payment is {d}")
    overpayment = int(total_payment - args.principal)
    print(f"Overpayment = {overpayment}")

elif args.type == "annuity":
    if args.principal and args.payment and args.interest:
        denominator = args.payment - 1 * args.principal
        if denominator <= 0:
            print("Incorrect parameters")
            sys.exit()
        n = math.ceil(math.log(args.payment / denominator, 1 + i))
        years = n // 12
        months = n % 12
        msg = "It will take "
        if years > 0:
            msg += f"{years} year{'s' if years > 1 else ''}"
        if years > 0 and months > 0:
            msg += " and "
        if months > 0:
            msg += f"{months} month{'s' if months > 1 else ''}"
        msg += " to repay this loan"
        print(msg)
        overpayment = int(args.payment * n - args.principal)
        print(f"Overpayment = {overpayment}")

    elif args.principal and args. periods and args.interest:
      annuity = args.principal * i * (1 + i) ** args.periods / ((1 + i) ** args.periods - 1)
      annuity = math.ceil(annuity)
      print(f"Your annuity payment = {annuity}")
      overpayment = int(annuity * args.periods - args.principal)
      print(f"Overpayment = {overpayment}")

    elif args.payment and args.periods and args.interest:
        principal = args.payment / (i * (1 + i) ** args.periods / ((1 + i) ** args.periods - 1))
        principal = math.floor(principal)
        print(f"Your loan principal = {principal}")
        overpayment = int(args.payment * args.periods - principal)
        print(f"Overpayment = {overpayment}")
    else:
        print(f"Incorrect parameters")
else:
    print("Incorrect parameters")

