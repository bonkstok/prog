import json

#data = {"Persoon":{"Naam": "Johnny","Leeftijd": 5,"Woonplaats": "Purmerend"},"Plaats":{"Stad": "Purmerend","Provincie": "Noord-Holland","Land": "Nederland"}}
print("Please enter the following information:")
naam = input("Wat is uw naam? ")
woonplaats = input("Wat is uw woonplaats? ")
nationaliteit = input("Wat is uw afkomst? ")
geslacht = input("Bent u man of vrouw? ")
data = {"Personal":{"Naam" : naam, "Woonplaats": woonplaats, "Nationaliteit": nationaliteit, "Geslacht": geslacht}, "BankInfo":{ "NaamBank": "Rabobank", "RekNummer": 142779504}}
print("Please enter a file name.")

textfile = input(">>") + ".json"

with open(textfile, 'w') as outfile:
	json.dump(data, outfile)
