import matplotlib.pyplot as plt
import requests
y_values = []

def get_data(currencyFrom, currencyTo):
	"""
		currencyFrom is the crypto currency like ETH, BTC etc
		currencyTo is the currency in which we have to convert
	"""
	#url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'.format(currencyFrom,currencyTo)

	#api for getting prices
	url = 'https://min-api.cryptocompare.com/data/price'
	
	#requesting api with query strings as passed in the params
	req = requests.get(url, params = {'fsym':currencyFrom, 'tsyms':currencyTo})

	#converting into json format
	content = req.json()

	#getting value of the cryptocurrency in the required currency
	crypto = content[currencyTo]

	return crypto
	

def plot_graph(crypto, currency):
	plt.title(crypto + " Visualization")
	plt.ylabel('Price in' + currency)
	while True:
		data = get_data(crypto, currency)
		y_values.append(data)
		plt.plot(y_values)
		plt.show
		plt.pause(1)

plot_graph('BTC', 'USD')