import requests
from bs4 import BeautifulSoup

URL = "https://elecnor-deimos.com/jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("li", class_='hentry')

# Look for Python jobs
jobs = results.find_all('li')
for job in jobs:
    link = job.find("a")["href"]
    print(job.text.strip())
    print(f"Apply here: {link}\n")
