import os
import requests
from bs4 import BeautifulSoup as bs4
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

# print(format_currency(5000, "KRW", locale="ko_KR"))

url = "https://www.iban.com/currency-codes"
url_converse="https://transferwise.com/gb/currency-converter/gbp-to-usd-rate?amount=50"

countries = []
currencies = []

request = requests.get(url)
soup = bs4(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countries.append(country)

def ask():
  try:
    print("Where are you from? Choose a country by number.")
    country_from = int(input("#: "))
    if country_from > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      print("Now Choose another Country.")
      country_to = int(input("#: "))
      if country_to > len(countries):
        print("Choose a number from the list.")
        ask()
      else :
        country_a = countries[country_from]
        country_b = countries[country_to]

        # url_converse
        converse(country_a, country_b)

  except ValueError:
    print("That wasn't a number.")
    ask()

def converse(country_a, country_b) :
  country_a_code = country_a['code']
  country_b_code = country_b['code']

  print(f"How many {country_a_code} do you want to convert to {country_b_code}")
  currency_input = int(input("#: "))
        
  currency_request = requests.get(f"https://transferwise.com/gb/currency-converter/{country_a_code.lower()}-to-{country_b_code.lower()}-rate?amount={currency_input}")
        
  currency_soup = bs4(currency_request.text, "html.parser")
        
  amount = currency_soup.find("input",{"class" : "js-TargetAmount"})["value"]
        
  print(f"{format_currency(currency_input,country_a_code)} is {format_currency(amount, country_b_code)}")

print("Welcome to CurrencyConvert PRO 2020:")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")

ask()

