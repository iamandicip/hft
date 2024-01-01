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
data = bt.feeds.YahooFinanceCSVData(dataname='TSLA.csv')
cerebro.adddata(data) 

# Add the strategy to cerebro 
cerebro.addstrategy(ScalpingStrategy, period=20, percent=0.01) 

cerebro.run() 

cerebro.plot() 