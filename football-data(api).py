import httplib
import bs4
import json
import csv
from wikipedia import *
from re import *
from bs4 import *

def parser(html):
	html=BeautifulSoup(html,"lxml")
	teams=[]
	for i in html.findAll('a'):
		for j in i:
			teams.append(j)
	return teams



connection = httplib.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'bc608ba18f034f468ab0d65ad7b9fceb', 'X-Response-Control': 'minified' }
# To get the ids for all seasons.
connection.request('GET','/v1/soccerseasons/?season=2015',None,headers)

response = json.loads(connection.getresponse().read())

ids=[]

for i in response:
	ids.append(i['id'])


for lt in ids:
	connection.request('GET', '/v1/soccerseasons/'+str(lt)+'/teams', None, headers )
	response = json.loads(connection.getresponse().read())

	for i in response['teams']:
		id1=i['id']
		connection1=httplib.HTTPConnection('api.football-data.org')
		headers1={'X-Auth-Token':'bc608ba18f034f468ab0d65ad7b9fceb' , 'X-Response-Control':'minified'}
		connection1.request('GET','/v1/teams/'+str(id1)+'/players',None,headers1)
		response1=json.loads(connection1.getresponse().read())
		for j in response1['players']:
				row=[]
				for k in j:
					if type(j[k])==int:
						row.append(j[k])
					else:
						try:
							row.append(str(j[k].encode('utf8')))
						except:
							row.append('NaN')
				print j['name']
				age=j['dateOfBirth']
				age=str(age[0:4])
				#print j['name']+" (footballer, born %s)"%age
				try:
					page1=page(j['name']+" (footballer, born %s)"%age)
					page1=page1.html()
					start1=page1.find(">Senior career*<")
					end1=page1.find(">National team<")
					page1=page1[start1:end1]
					teams=parser(page1)
					teams1=""
					for k in teams:
						teams1=teams1+str(k.encode('utf8'))+", "
					row.append(teams1)
					print teams1
					f=open('PlayerDatabase.csv','a')
					writ=csv.writer(f)
					writ.writerow(row)
					f.close()
					print " *\n"
				except:
					continue
			#print j['name'],teams1
			