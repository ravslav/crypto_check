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


"""
{
    "time": {
        "updated": "Dec 4, 2023 20:04:00 UTC",
        "updatedISO": "2023-12-04T20:04:00+00:00",
        "updateduk": "Dec 4, 2023 at 20:04 GMT",
    },
    "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
    "chartName": "Bitcoin",
    "bpi": {
        "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "40,763.4025",
            "description": "United States Dollar",
            "rate_float": 40763.4025,
        },
        "GBP": {
            "code": "GBP",
            "symbol": "&pound;",
            "rate": "34,061.5730",
            "description": "British Pound Sterling",
            "rate_float": 34061.573,
        },
        "EUR": {
            "code": "EUR",
            "symbol": "&euro;",
            "rate": "39,709.5055",
            "description": "Euro",
            "rate_float": 39709.5055,
        },
    },
}"""
