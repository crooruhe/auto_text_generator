import requests
import json


class true_random:
	def __init__(self, num):
		self.num = num
	def get_true_rand(self):
		# *********************************************************
		# random.org allows for free developer api tokens
		# insert your api token below
		rand_api_token = 'YOUR_API_KEY_HERE'
		url = 'https://api.random.org/json-rpc/4/invoke'

		data = {
			"jsonrpc": "2.0",
			"method": "generateIntegers",
			"params": {
				"apiKey": "40e830cb-f075-483e-bdeb-83f5902a7743",
				"n": 1,
				"min": 1,
				"max": self.num,
				"replacement": True,
				"base": 10,
				#"pregeneratedRandomization" : null
			},
			"id": 19030
		}

			
		r = requests.post(url, json = data).json()

		final_rando_num = (r["result"]["random"]["data"][0])

		return(final_rando_num)