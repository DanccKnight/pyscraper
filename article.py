from newspaper import Article
from bs4 import BeautifulSoup
import requests
import nltk
#nltk.download("punkt")

web_url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"

r = requests.get(web_url)
soup = BeautifulSoup(r.text,'html.parser')
link_set = soup.find_all('a', class_ = "DY5T1d")
count = 5
base = "https://news.google.com/"

for i in soup.find_all('a', class_ = "DY5T1d"):
    if(count==0):
        break
    str = base + i['href']
    darticle = Article(str)
    
    darticle.download()
    darticle.parse()
    darticle.nlp()
    
    print("\nTitle:" + darticle.title)
    print("\nSummary:" + darticle.summary)
    count = count - 1

