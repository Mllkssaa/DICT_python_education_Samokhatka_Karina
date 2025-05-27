import requests


mycoins = float(input("Please, enter the number of mycoins you have. >"))
rate = float(input("Please, enter the exchange rate. >"))
print(f"The total amount of dollars.--> {round(mycoins * rate, 2)}")

mycoins = float(input("Enter amount of mycoins. >"))
rates = {
    'ARS': 0.82,
    'HNL': 0.17,
    'AUD':1.9622,
    'MAD': 0.208
}
for currently, rate in rates.items():
    converted = round(mycoins * rate, 2)
    print(f"I will get {converted} {currently} from the sale of {mycoins} mycoins.")
