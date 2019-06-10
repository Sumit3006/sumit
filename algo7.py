import bs4 as bs
import datetime as dt
import os
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import pickle
import requests

def save_sp500_tickers():
    resp=requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup=bs.BeautifulSoup(resp.text,"lxml")
    table=soup.find('table',{'class':'wikitable sortable'})
    tickers=[]
    for row in table.findAll('tr')[1:]:
         ticker=row.findAll('td')[0].text
         tickers.append(ticker)
    with open("sp500tickers.pickle","wb")as f:
         pickle.dump(tickers,f)

         print(tickers)    

         return tickers
#save_sp500_tickers()
def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers=sp_500_tickers()
    else:
        with open("sp500tickers.pickle","rb")as f:
            tickers=pickle.load(f)
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    start=dt.datetime(2000,1,1)
    end=dt.datetime(2016,12,31)
    

    for ticker in tickers[:100]:
        print(ticker)
        tic=ticker.strip("\n")
        if not os.path.exists('stock_dfs/{}.csv'.format(tic)):
            yf.pdr_override()
            df=yf.download(tic,start,end)
            df.to_csv('stock_dfs/{}.csv'.format(tic))
        else:
            print('Already have {}'.format(tic))
get_data_from_yahoo()    
