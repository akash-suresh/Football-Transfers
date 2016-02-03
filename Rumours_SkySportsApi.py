import httplib
import bs4
import json

connection = httplib.HTTPConnection('skysportsapi.herokuapp.com')
headers = { 'X-Response-Control': 'minified' }
connection.request('GET', '/sky/getnews/football/v1.0/', None, headers )
response = json.loads(connection.getresponse().read().decode())

#print response
for i in response:
	print i['shortdesc'],"\n"



