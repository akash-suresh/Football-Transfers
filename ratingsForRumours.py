from selenium import webdriver
from urllib2 import urlopen
import time
import bs4



browser = webdriver.Firefox()

browser.get('https://www.google.co.in')

searchID= browser.find_element_by_id('lst-ib')
searchID.send_keys('Cristiano Ronaldo')
searchID.submit()
time.sleep(5)
browser.find_element_by_css_selector('.button.lsb').click()


print browser.current_url

page2=urlopen(browser.current_url)

content=page2.read()

soup=bs4.BeautifulSoup(content,'html.parser')

print soup.prettify()

div1=soup.find('div',id="resultStats")

print div1

