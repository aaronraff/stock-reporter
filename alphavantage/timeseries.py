import urllib.request as req
import ssl
import json

class TimeSeries:
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
		return the parsed JSON stock data
		"""
		try:
			context = ssl._create_unverified_context()
			url = ("https://www.alphavantage.co/query?" +
				"function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + symbol + 
				"&apikey=" + self.api_key)
			data = req.urlopen(url, context=context).read()
			data = self.__parse(data)

			return data
		except Exception as e:
			print("There was an error getting the data that you requested.")
			return None

	def __parse(self, data):
		"""
		Parse JSON data.

		param: data - the contents to be parsed
		return: the parsed JSON
		"""
		return json.loads(data)	
