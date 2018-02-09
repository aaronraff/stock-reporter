from config import api_key
from alpha_vantage import AlphaVantage

def getCurrentPrice(prices):
	meta = data["Meta Data"]
	lastUpdated = meta["3. Last Refreshed"]
	ts = data["Time Series (Daily)"]
	#get the first word (the date)
	date = lastUpdated.split()[0]
	price = ts[date]["5. adjusted close"]
	return price

def makeList(data):
	#need last updated to get the JSON element later
	meta = data["Meta Data"]
	interval = meta["4. Interval"]
	lastUpdated = meta["3. Last Refreshed"]
	ts = data["Time Series (" + interval + ")"]
	mr = ts[lastUpdated]
	return [mr["1. open"], mr["2. high"], mr["3. low"], mr["4. close"]]

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
