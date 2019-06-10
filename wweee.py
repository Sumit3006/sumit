import datetime as dt
import os
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import csv
import pickle
data=pd.read_csv('C:/Users/Sumit/Downloads/data.csv')
securityid=[]
securityid=data['Symbol'].values
s='.NP'
newid=[x+s for x in securityid]
print(newid)
if not os.path.exists('bselist_stocks'):
    os.makedirs('bselist_stocks')
start=dt.datetime(2010,1,1)
end=dt.datetime(2019,5,30)
for myid in newid:
    print(myid)
    if not os.path.exists('bselist_stocks/{}.csv'.format(myid)):
        yf.pdr_override()
        df=yf.download(myid,start,end)
        df.to_csv('bselist_stocks/{}.csv'.format(myid))
    else:
        print('Already exists{}'.format(myid))
        
    
