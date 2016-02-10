import bs4
import urllib2
import requests
import csv

def parse(res):
	
	divs=res.findAll("div",{"class" : "lc-title-container"})
	#f=open('news_sky.csv','a')
	for div in divs:
		f=open('news_sky.csv','a')
		writ=csv.writer(f)
		row=[]
		row.append(str((div.getText()).encode('utf-8'))+"\n")
		writ.writerow(row)
		f.close()		

txt=requests.get("http://www.dailymail.co.uk/sport/football/article-3420432/Transfer-news-LATEST-Arsenal-Liverpool-Manchester-United-latest-plus-Premier-League-rest-Europe.html")
txt.raise_for_status()
soup=bs4.BeautifulSoup(txt.text)
parse(soup)