# filename: stock_price_chart.py
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical stock price data for NVDA and TSLA
nvda = yf.download("NVDA", start="2022-01-01", end="2022-12-31")
tsla = yf.download("TSLA", start="2022-01-01", end="2022-12-31")

# Plot the stock price change
plt.plot(nvda['Close'], label='NVDA')
plt.plot(tsla['Close'], label='TSLA')

# Set the chart title and labels
plt.title('NVDA and TSLA Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')

# Add a legend
plt.legend()

# Display the chart
plt.show()