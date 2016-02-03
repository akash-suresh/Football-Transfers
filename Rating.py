import bs4
from urllib2 import urlopen 

cust="http://sofifa.com/players?keyword="

player=raw_input().split(' ')
cust+='+'.join(player)

page=urlopen(cust)

content = page.read()
soup=bs4.BeautifulSoup(content,'html.parser')

news=soup.find_all('td')

for a in news:
	b=a.get('date-title')
	print a.get_text()
