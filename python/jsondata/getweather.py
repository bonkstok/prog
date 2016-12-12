#!/usr/bin/python3
import json
import requests
import sys


def getWeather():
	location = input("Please enter a city:")
	try:
		response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid=44db6a862fba0b067b1930da0d769e98'.format(location))
		#return response
	except requests.exceptions.ConnectionError as e:
		return e
	jdata = response.json()
	#print(jdata)
	plaats = jdata["name"]
	tempKelvin = jdata["main"]["temp"]
	tempCelcius = tempKelvin - 273.15
	description = jdata["weather"][0]["description"]
	print("Het is nu {}{:.2f} graden in {}. Het is {}".format('', tempCelcius , plaats, description))
	#print("Het is nu {}{:.2f}".format('', tempCelcius))
	print("Plaats:\t\t{}".format(plaats))
	print("Graden:\t\t{}{:.0f}".format('',tempCelcius))
	print("Beschrijving\t{}".format(description))
	print("----------------------------------------")
	print("Do you wish to get the weather forcast for another city? Y for yes, any other character for no.")
	decision = input(">>")
	if decision is "y" or decision is "Y":
		getWeather()
	else:
		#close the program
		sys.exit()


def main():
	getWeather()
	

if __name__ == '__main__':
	main()