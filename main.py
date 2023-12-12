import requests
from bs4 import BeautifulSoup

url = 'https://tengrinews.kz/news/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

titles = soup.find_all("span", class_='tn-article-title')

for title in titles:
    print(title.text.strip())
