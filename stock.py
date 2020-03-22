import requests
from bs4 import BeautifulSoup
import re

def getData(web_url):
    r = requests.get(web_url)
    soup = BeautifulSoup(r.text,'html.parser')
    td = soup.find_all('td',class_='brdrgtgry')

    for i in td:
        print(i.text)

web_url = "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9"

getData(web_url)
