from urllib.request import urlopen
import json
mode = input('Driving or walking?')
bestemming = input('Adres:')
bestemming = bestemming.split(',')
print(bestemming)

#url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=Oostervenne+239+Purmerend&destinations=rijksdorp+wassenaar&mode=driving&key=AIzaSyC6lUl5i5cDy3ryvoblgoLOhsovHAP7-Ls'
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins={}+{}+{}&destinations=maastricht+Nederland&mode={}&key=-Ls'.format(bestemming[0],bestemming[1],bestemming[2],mode)
response = urlopen(url)
print(url)
data = json.loads(response.read().decode('utf-8'))
#print(data)
km =  data['rows'][0]['elements'][0]['distance']['text']
km = km[:-2]
print(km)
