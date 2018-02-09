import urllib.request as req
import ssl
import json

class AlphaVantage:
	"""
	Wrapper for https://www.alphavantage.co.
	"""
	def __init__(self, api_key):
		"""
		Constructs a new AlphaVantage object.

		param: api_key - the api key to use for requests
		"""
		self.api_key = api_key

	def getStockData(self, symbol):
		"""
		Get the stock data from the api.

		param: symbol - the stock symbol to retrieve
		"""
		context = ssl._create_unverified_context()
		url = ("https://www.alphavantage.co/query?" +
			"function=TIME_SERIES_INTRADAY&symbol=" + symbol + 
			"&interval=1min&apikey=" + self.api_key)
		data = req.urlopen(url, context=context).read()
		data = self.__parse(data)
		print(data["Meta Data"])

	def __parse(self, data):
		"""
		Parse JSON data.

		param: data - the contents to be parsed
		return: the parsed JSON
		"""
		return json.loads(data)	
