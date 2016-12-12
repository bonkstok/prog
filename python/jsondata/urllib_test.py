import urllib.request
import urllib.parse
#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())
'''
url = 'https://pythonprogramming.net'
values = {'s': 'basic',
            'submit':'search'}
data = urllib.parse.urlencode(values)
print(url+data)
data = data.encode('utf-8') #put your to bits

req = urllib.request.Request(url,data)
print(req)
resp = urllib.request.urlopen(req)
restData = resp.read()
#encode like s=basic&submit=search]
print(restData)
'''
# try:
#     x = urllib.request.urlopen('https://www.google.com/search?q=test')
#     print(x.read())
#
# except Exception as e:
#     print(str(e))


try:
    url = 'https://www.google.com/search?q=test'
    headers = {} # data you ssend in, contains information who you are.. OS, Browser etc
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    #print(respData)
    saveFile = open('heade.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))
