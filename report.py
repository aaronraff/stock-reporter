from config import api_key
from alpha_vantage import AlphaVantage

#create new instance of AlphaVantage wrapper
api = AlphaVantage(api_key)

#get the user's input
print("What stock (symbol) are you looking for?")
symbol = input()

api.getStockData(symbol)
