import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    url = f'https://www.finn.no/job/fulltime/search.html?abTestKey=rerank&industry=65&location=1.20001.20061&location=1.20001.22030&page={page}&sort=RELEVANCE'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

    
def tansform(soup):
    article = soup.find_all('article', class_ = 'ads__unit')
    for item in article:
        company = item.find('div', class_='ads__unit__content__list').text
        location = item.find('div', class_='ads__unit__content__details').text
        link = item.a['href']
        try:
            title = item.find('div', class_= 'ads__unit__content__keys').text
        except:
            title = 'Not definde'
            
        
        job = {
            'company' : company,
            'title' : title,
            'location' : location,
            'link' : link
        }
        joblist.append(job)
    return

joblist = []
for i in range(0,20):
    print(f'laddar information, {i}')
    c = extract(1)
    tansform(c)

df = pd.DataFrame(joblist)

print(df.head())
df.to_csv('jobsfinn.csv')
