from newspaper import Article
from bs4 import BeautifulSoup
import requests
import nltk
#nltk.download("punkt")

def search(soup):
    results = soup.find_all(text="Union",recursive=True)
    print(len(results))

web_url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"

r = requests.get(web_url)
soup = BeautifulSoup(r.text,'html.parser')
base = "https://news.google.com/"
count = 5

for i in soup.find_all('a', class_ = "DY5T1d"):
    if(count==0):
        break
    str = base + i['href']
    article = Article(str)
    
    article.download()
    article.parse()
    article.nlp()
    
    print("\nTitle:" + article.title)
    print("Summary:" + article.summary)
    count = count - 1

search(soup)
