from config import api_key
from alpha_vantage import AlphaVantage

def getCurrentPrice(prices):
	#divide by 4 becuase high, low, open, close
	return sum(prices)/4

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
prices = map(float, makeList(data))
print(getCurrentPrice(prices))
