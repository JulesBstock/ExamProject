import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web

beg = datetime.date(2005, 1, 1)
end = datetime.date(2015, 12, 31)

AAPL = web.DataReader("AAPL", 'yahoo', beg, end)
AXP = web.DataReader("AXP", 'yahoo', beg, end)
FDX = web.DataReader("FDX", 'yahoo', beg, end)
GOOGL = web.DataReader("GOOGL", 'yahoo', beg, end)
IBM = web.DataReader("IBM", 'yahoo', beg, end)
KO = web.DataReader("KO", 'yahoo', beg, end)
MS = web.DataReader("MS", 'yahoo', beg, end)
NOK = web.DataReader("NOK", 'yahoo', beg, end)
XOM = web.DataReader("XOM", 'yahoo', beg, end)
YHOO = web.DataReader("YHOO", 'yahoo', beg, end)

AAPL['Date'] = AAPL.index.map(lambda x: str(x)[:10])
AXP['Date'] = AXP.index.map(lambda x: str(x)[:10])
FDX['Date'] = FDX.index.map(lambda x: str(x)[:10])
GOOGL['Date'] = GOOGL.index.map(lambda x: str(x)[:10])
IBM['Date'] = IBM.index.map(lambda x: str(x)[:10])
KO['Date'] = KO.index.map(lambda x: str(x)[:10])
MS['Date'] = MS.index.map(lambda x: str(x)[:10])
NOK['Date'] = NOK.index.map(lambda x: str(x)[:10])
XOM['Date'] = XOM.index.map(lambda x: str(x)[:10])
YHOO['Date'] = YHOO.index.map(lambda x: str(x)[:10])

class Stock(object):
    def __init__(self, term, amount, stock, date):
        self.term = term
        self.amount = amount
        self.date = date
        if stock == "AAPL":
            self.stock = "AAPL"
            self.df = AAPL
        elif stock == "AXP":
            self.stock = "AXP"
            self.df = AXP
        elif stock == "FDX":
            self.stock = "FDX"
            self.df = FDX
        elif stock == "GOOGL":
            self.stock = "GOOGL"
            self.df = GOOGL
        elif stock == "IBM":
            self.stock = "IBM"
            self.df = IBM
        elif stock == "KO":
            self.stock = "KO"
            self.df = KO
        elif stock == "MS":
            self.stock = "MS"
            self.df = MS
        elif stock == "NOK":
            self.stock = "NOK"
            self.df = NOK
        elif stock == "XOM":
            self.stock = "XOM"
            self.df = XOM
        elif stock == "YHOO":
            self.stock = "YHOO"
            self.df = YHOO
        else:
            self.stock = False
            self.df = False


x1 = AAPL['High'].plot(label='AAPL')
x2 = AXP['High'].plot(label='AXP')
x3 = FDX['High'].plot(label='FDX')
x4 = GOOGL['High'].plot(label='GOOGL')
x5 = IBM['High'].plot(label='IBM')
x6 = KO['High'].plot(label='KO')
x7 = MS['High'].plot(label='MS')
x8 = NOK['High'].plot(label='NOK')
x9 = XOM['High'].plot(label='XOM')
x10 = YHOO['High'].plot(label='YHOO')

x1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.show()

