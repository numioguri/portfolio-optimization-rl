import yfinance as yf

tickers = ['AAPL', 'MSFT', 'GOOGL']

# Download stock data
data = yf.download(tickers, start="2020-01-01", end="2024-12-31")

# Extract only the 'Close' prices
close_prices = data['Close']
close_prices.to_csv('stocks.csv')

print("Stock close prices saved successfully in stocks.csv")
