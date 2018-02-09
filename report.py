from config import api_key
from alpha_vantage import AlphaVantage

api = AlphaVantage(api_key)
api.getStockData("MSFT")
