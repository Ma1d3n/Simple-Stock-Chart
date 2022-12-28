import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Get the stock data for a specific ticker
ticker = yf.Ticker(input("Ticker "))
data = ticker.history(period="max")

# Create a dataframe with the OHLC data for the chart
df = pd.DataFrame({
    'open': data['Open'],
    'high': data['High'],
    'low': data['Low'],
    'close': data['Close']
})

# Calculate the SMA 200
df['sma200'] = df['close'].rolling(window=200).mean()

# Create the candlestick chart
fig = go.Figure(data=[
    go.Candlestick(x=df.index.tolist(), open=df['open'], high=df['high'], low=df['low'], close=df['close']),
    go.Scatter(x=df.index.tolist(), y=df['sma200'], name='SMA 200', line=dict(color='blue'))
])

# Show the chart
fig.show()

