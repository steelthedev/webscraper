from bs4 import BeautifulSoup
import requests

source=requests.get('http://thenetnaija.com').text

soup=BeautifulSoup(source,'lxml')

content_main=soup.find('div',class_="file-one-shadow")

#print(content_main.prettify())

title=content_main.a

print(title)