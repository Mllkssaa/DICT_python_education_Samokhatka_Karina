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
        response.raise_for_status()
        data = response.json()
        usd = data.get("usd", {}).get("rate")
        eur = data.get("eur", {}).get("rate")
        return usd, eur, data
    except Exception:
        return None, None, None

while True:
    currency_code = input("Please enter the currency code (e.g., AUD): ").strip().lower()
    if len(currency_code) != 3 or not currency_code.isalpha():
        print("Invalid input. Please enter a 3-letter currency code (e.g., USD, EUR, AUD).")
        continue

    usd_rate, eur_rate, rates_data = get_exc_rate(currency_code)
    if usd_rate is None or eur_rate is None:
        print("Currency not found or error retrieving exchange rates. Please try again.")
    else:
        print(f"Exchange rate for {currency_code.upper()}: {usd_rate:.2f} USD, {eur_rate:.2f} EUR")
        break


cache = {}

currency_base = currency_code.lower()
cache.update({
    'usd': rates_data.get("usd", {}),
    'eur': rates_data.get("eur", {})
})

while True:
    currency_target = input("Enter the target currency code (or press Enter to exit). >").lower()
    if not currency_target:
        break
    amount = float(input("Enter the amount you want to exchange. >"))
    if currency_target in cache:
        print("Checking the cache... please wait...")
        rate = cache[currency_target]["rate"]
    else:
        print("Sorry, but it is not in the cache!")
        new_rates = requests.get(f"http://www.floatrates.com/daily/{currency_base}.json").json()
        if currency_target in new_rates:
            rate = new_rates[currency_target]["rate"]
            cache[currency_target] = new_rates[currency_target]
        else:
            print("Sorry, this currency is not available..")
            continue

    converted_amount = round(amount * rate, 2)
    print(f"You received {converted_amount} {target_currency.upper()}!")