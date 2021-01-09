import requests
from bs4 import BeautifulSoup

URL = "https://www.tipranks.com/news/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("h3", class_='fontSize5')

print('test')
