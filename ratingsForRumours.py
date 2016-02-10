import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from bs4 import *

import csv
f = open('news_sky.csv', 'rb')
writ = open('Ratings.csv','w')
reader = csv.reader(f)
txt=[]
for row in reader:
    for j in row:
    	flag=True
    	if len(j)<8:
    		continue
    	for k in range(0,len(txt)):
    		if j==txt[k]:
    			flag=False
    	if flag==False:
    		continue
    	try :
    		inp=[]
    		browser = webdriver.Firefox()
    		browser.get('http://www.google.com')
    		search = browser.find_element_by_name('q')
    		search.send_keys(j)
    		inp.append(j)
    		search.send_keys(Keys.RETURN) # hit return after you enter search text
    		time.sleep(5) # sleep for 5 seconds so you can see the results
    		html1=browser.page_source
    		browser.quit()
    		soup=BeautifulSoup(html1,'lxml')
    		div1= soup.find("div",{"id":"resultStats"})
    		temp=''.join(map(str,div1.contents))
    		x=temp.find("About")
    		y=temp.find("results")
    		inp.append(temp[x+5:y])
    		wrt=csv.writer(writ)
    		wrt.writerow(inp)
    	except :
    		continue
f.close()
writ.close()

'''
browser = webdriver.Firefox()
browser.get('http://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("\n\nBournemouth forward Lee Tomlin joins Bristol City on loan\n")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

html1=browser.page_source
browser.quit()
soup=BeautifulSoup(html1,'lxml')

div1= soup.find("div",{"id":"resultStats"})

temp=''.join(map(str,div1.contents))
x=temp.find("About")
y=temp.find("results")
print temp[x+5:y]

'''