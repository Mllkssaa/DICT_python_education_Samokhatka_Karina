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

def get_exc_rate(currency_code):
    url = f"https://www.floatrates.com/daily/{currency_code.lower()}.json"
    try:
        response = requests.get(url)
        data = response.json()
        usd = data.get("usd", {}).get("rate")
        eur = data.get("eur", {}).get("rate")
        return usd, eur, data
    except Exception as e:
        return None, None, None

while True:
    currency_code = input("Please enter the currency code (e.g., AUD). >").strip().lower()
    if len(currency_code) !=3 or not currency_code.isalpha():
        print("Invalid input. Please enter a 3-letter currency code (e.g., USD, EUR, AUD)..")
        continue

    usd_rate, eur_rate, rates_data = get_exc_rate(currency_code)
    if usd_rate is None or eur_rate is None:
        print("Currency not found or error retrieving exchange rates. Please try again.")
    else:
        print(f"Exchange rate for {currency_code.upper()}: {usd_rate} USD, {eur_rate} EUR")
        break