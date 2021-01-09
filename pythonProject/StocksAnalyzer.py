import plotly.express as px
import yfinance as yf
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

# date times setting
old = datetime.now() - timedelta(days=30)  # current date and time
now = datetime.now()  # current date and time
str_old = old.strftime("%Y-%m-%d")
str_now = now.strftime("%Y-%m-%d")

# web scraping for news
URL = "https://www.tipranks.com/news/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
newsHeaders = soup.find_all("h3", class_='fontSize5')

# downloading stocks data from yahoo finance
stocks = ["BNGO", "TRXC"]

data = yf.download(stocks, start=str_old, end=str_now)
data.head()
openStocks = data.loc[:, "Open"].copy()
closedStocks = data.loc[:, "Close"].copy()

# charting data from yahoo finance
closedStocks.plot(figsize=(14, 8), fontsize=15)
norm = closedStocks.div(closedStocks.iloc[0]).mul(300)
df = px.data.stocks()

fig = px.line(closedStocks, x=closedStocks.index, y=closedStocks.columns)
fig.update_xaxes(
    dtick="M1",
    tickformat="%d %B (%a)<br>%Y")
fig.show()
