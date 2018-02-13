from config import api_key
from alphavantage.timeseries import TimeSeries

#create new instance of AlphaVantage wrapper
api = TimeSeries(api_key)

#get the user's input
print("What stock (symbol) are you looking for?")
symbol = input()

data = api.getStockData(symbol)
currentPrice = api.getCurrentPrice(data)

#alpha_vantage.getStockData returns None if there is an error
if data != None:
	print(currentPrice)
else:
	print("There was an error getting the data.")
