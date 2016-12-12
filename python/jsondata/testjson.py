#!/usr/bin/python3
#json data
import json
from pprint import pprint
def main():
	# data = [{'a':'A', 'b':(2,4), 'c':3.0}]
	# print('DATA:{}'.format(repr(data)))
	# data_string = json.dumps(data)
	# print("JSON:", data_string)
	datas = {"Persoon":{"Naam": "Johnny","Leeftijd": 5,"Woonplaats": "Purmerend"},"Plaats":{"Stad": "Purmerend","Provincie": "Noord-Holland","Land": "Nederland"}}
	
	print(datas["Persoon"]["Woonplaats"])
	n = json.dumps(datas)
	o = json.loads(n)
	print(o)
	print(o["Persoon"]["Naam"])




	#data_string = json.dumps(data)
	#print("Encoded:", data_string)


	#encode json
	# data_string = json.dumps(data)
	# print(data_string)
	# decoded = json.loads(data_string)
	# print(decoded)
	# print(data_string['Persoon']['Woonplaats'])





	#decoded = json.loads(data_string)
	#print("Decoded:", decoded)
	#response = decoded.json()
	#print(data["Persoon"]["Naam"])
	#print(data[0]["Persoon"]["Naam"])

	#print("Original:", type(data[0]['b']))
	
	#print("Decoded:", type(decoded[0]['b']))
	with open('persoon.json') as data_file:
		data = json.load(data_file)
	print("Naam:\t\t",data["Persoon"]["Naam"])
	print("Woonplaats:\t", data["Persoon"]["Woonplaats"])
	print("Land:\t\t", data["Plaats"]["Land"])
	print("{} ligt in {}, en {} ligt vervolgens weer in {}".format(data["Persoon"]["Woonplaats"], data["Plaats"]["Provincie"], data["Plaats"]["Provincie"],data["Plaats"]["Land"]))



if __name__ == '__main__':
	main()