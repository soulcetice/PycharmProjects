import plotly.express as px
import yfinance as yf

stocks = ["AAPL", "TSLA", "PLTR", "SBUX"]

data = yf.download(stocks, start="2017-01-01", end="2020-11-30")

data.head()

closedStocks = data.loc[:, "Close"].copy()

closedStocks.plot(figsize=(14, 8), fontsize=15)

norm = closedStocks.div(closedStocks.iloc[0]).mul(200)

df = px.data.stocks()

fig = px.line(closedStocks, x=closedStocks.index, y=closedStocks.columns)

fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")

fig.show()
