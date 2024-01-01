# Backtrader

Basic bot for a scalping strategy using Python and the popular backtesting library called Backtrader. 

This strategy is a simplified version and serves as a starting point for testing and further customization: 

```python
import datetime
import backtrader as bt 

class ScalpingStrategy(bt.Strategy): 
  params = ( ('period', 20), ('percent', 0.01) ) 
  
  def __init__(self): 
    self.sma = bt.indicators.SimpleMovingAverage(self.data, period=self.params.period) 
    
  
  def next(self): 
    if self.data.close[0] > self.sma[0] + (self.sma[0] * self.params.percent): 
      self.buy() 
    if self.data.close[0] < self.sma[0] - (self.sma[0] * self.params.percent): 
      self.sell() 
      
# Define indicator parameters 
fast_ma_period = 10 
slow_ma_period = 50 

# Create a cerebro instance 
cerebro = bt.Cerebro() 

# Add data feed to cerebro 
data = bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=datetime(2019, 1, 1), todate=datetime(2020, 1, 1)) 
cerebro.adddata(data) 

# Add the strategy to cerebro 
cerebro.addstrategy(ScalpingStrategy, period=20, percent=0.01) 

cerebro.run() 

cerebro.plot() 
``` 

In this example, we define a `ScalpingStrategy` class that inherits from `bt.Strategy`. 

The strategy uses a simple moving average (SMA) indicator with a specified period. The `next` method is called on each new data point, where we check if the current price is above or below the SMA with a certain percentage difference. If it is, we place a buy or sell order, respectively. 

To add more detailed indicators, you can include additional indicators in the `__init__` method of the strategy, such as relative strength index (RSI), MACD, or Bollinger Bands. 

These indicators can be accessed and used within the `next` method just like the SMA in the example. 

Remember to backtest and modify this sample bot according to your specific requirements and risk tolerance before deploying it in live trading.