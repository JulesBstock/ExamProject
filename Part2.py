import os
import glob
import pandas as pd
import numpy as np
import webbrowser
import datetime
import matplotlib.pyplot as plt
import random
import pandas_datareader.data as web

path = "C:/Users/jules/Documents/M2/Python/ExamProject/Data"
allfiles = glob.glob(os.path.join(path,"*.csv"))


np_array_list = []
for file in allfiles:
    df = pd.read_csv(file, sep=';', index_col=0, parse_dates=True)
    #np_array_list.append(df.as_matrix())
    #print(df)
#comb_np_array = np.vstack(np_array_list)
#big_frame = pd.DataFrame(comb_np_array)

#print(big_frame)
#Yahoo = df.ix[:,0]
#print(Yahoo)

start = datetime.date(2005, 1, 1)
end = datetime.date(2015, 12, 31)
AAPL=web.DataReader("AAPL", 'yahoo', start, end)
GOOGL=web.DataReader("GOOGL", 'yahoo', start, end)
YHOO=web.DataReader("YHOO", 'yahoo', start, end)
AXP= web.DataReader("AXP", 'yahoo', start, end)
XOM =web.DataReader("XOM", 'yahoo', start, end)
KO= web.DataReader("KO", 'yahoo', start, end)
NOK= web.DataReader("NOK", 'yahoo', start, end)
MS=web.DataReader("MS", 'yahoo', start, end)
IBM= web.DataReader("IBM", 'yahoo', start, end)
FDX=web.DataReader("FDX", 'yahoo', start, end)
AAPL['Date'] =AAPL.index.map(lambda x: str(x)[:10])
GOOGL['Date'] =GOOGL.index.map(lambda x: str(x)[:10])
YHOO['Date'] =YHOO.index.map(lambda x: str(x)[:10])
AXP['Date'] =AXP.index.map(lambda x: str(x)[:10])
XOM['Date'] =XOM.index.map(lambda x: str(x)[:10])
KO['Date'] =KO.index.map(lambda x: str(x)[:10])
NOK['Date'] =NOK.index.map(lambda x: str(x)[:10])
MS['Date'] =MS.index.map(lambda x: str(x)[:10])
IBM['Date'] =IBM.index.map(lambda x: str(x)[:10])
FDX['Date'] =FDX.index.map(lambda x: str(x)[:10])

class Stock(object):
    def __init__(self,term,amount,stockname,date):
        self.term=term
        self.amount=amount
        self.date=date
        if stockname=="AAPL":
            self.stockname = "AAPL"
            self.df= AAPL
        elif stockname=="GOOGL":
            self.stockname="GOOGL"
            self.df = GOOGL
        elif stockname == "YHOO":
            self.stockname = "YHOO"
            self.df = YHOO
        elif stockname == "AXP":
            self.stockname = "AXP"
            self.df = AXP
        elif stockname == "XOM":
            self.stockname = "XOM"
            self.df = XOM
        elif stockname == "KO":
            self.stockname = "KO"
            self.df = KO
        elif stockname == "NOK":
            self.stockname = "NOK"
            self.df = NOK
        elif stockname == "MS":
            self.stockname = "MS"
            self.df = MS
        elif stockname == "IBM":
            self.stockname = "IBM"
            self.df = IBM
        elif stockname == "FDX":
            self.stockname = "FDX"
            self.df = FDX
        else:
            self.stockname=False
            self.df=False


a=AAPL['High'].plot(label='Apple')
b=GOOGL['High'].plot(label='Google')
c=YHOO['High'].plot(label='Yahoo')
d=AXP['High'].plot(label='American Express Company')
e=XOM['High'].plot(label='Exxon')
f=KO['High'].plot(label='Coca-Cola')
g=NOK['High'].plot(label='Nokia')
h=MS['High'].plot(label='Microsoft')
i=IBM['High'].plot(label='IBM')
j=FDX['High'].plot(label='Fedex')

# Put a legend to the right of the current axis
a.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
