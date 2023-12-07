import requests
import sys

try:
    # getting whole response fron web page
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # json file is a dictionary so i am assingning it to a variable full_dict
    full_dict = response.json()
except requests.RequestException:
    pass

# getting to the value of rate_float
if "bpi" in full_dict:
    bt_currency = full_dict["bpi"]
    currency_usd = bt_currency["USD"]
    #print(currency_usd["rate_float"])

while True:
    try:
        if float(sys.argv[1]):
            amount = currency_usd["rate_float"] * float(sys.argv[1])
            print(f"${amount:,.4f}")
            break
    except requests.RequestException:
        sys.exit("Błąd")

