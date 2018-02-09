from config import api_key
from alpha_vantage.timeseries import AlphaVantage

def getCurrentPrice(data):
	"""
	Get the current price from the data

	param: data - the json data to get the current price from
	return: the current price from the data provided
	"""
	meta = data["Meta Data"]
	lastUpdated = meta["3. Last Refreshed"]
	ts = data["Time Series (Daily)"]
	#get the first word (the date)
	date = lastUpdated.split()[0]
	price = ts[date]["5. adjusted close"]
	return price

#create new instance of AlphaVantage wrapper
api = AlphaVantage(api_key)

#get the user's input
print("What stock (symbol) are you looking for?")
symbol = input()

data = api.getStockData(symbol)

#alpha_vantage.getStockData returns None if there is an error
if data != None:
	print(getCurrentPrice(data))
else:
	print("There was an error getting the data.")
