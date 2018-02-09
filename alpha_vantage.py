import urllib.request as req
import ssl

class AlphaVantage:
	def __init__(self, api_key):
		self.api_key = api_key

	def getStockData(self, symbol):
		context = ssl._create_unverified_context()
		url = ("https://www.alphavantage.co/query?" +
			"function=TIME_SERIES_INTRADAY&symbol=" + symbol + 
			"&interval=1min&apikey=" + self.api_key)
		print(req.urlopen(url, context=context).read())