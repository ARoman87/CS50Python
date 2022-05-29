import sys
import requests
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response = response.json()["bpi"]["USD"]["rate"]
response = response.replace(",", "")
response = float(response)


try:
    if sys.argv[1].isdigit():
        sys.argv[1] = float(sys.argv[1])
        num = response * sys.argv[1]
        print(f"${num:,.4f}")
    elif "." in sys.argv[1]:
        sys.argv[1] = float(sys.argv[1])
        num = response * sys.argv[1]
        print(f"${num:,.4f}")
    else:
        sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
