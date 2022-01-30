from datetime import date
from nsepy import get_history
import requests
import pandas as pd
from bs4 import BeautifulSoup
import operator
pd.set_option('max_columns', None)

d = {}
def get_data(st,size):
    i=0
    for s in st:
        
        stock_fut = get_history(symbol=s,
                            start=date(2022,1,28),
                            end=date(2022,1,28),
                            futures=True,
                            expiry_date=date(2022,2,24))
        print(stock_fut)                    
        stock_fut.drop(['Open','High','Low','Close','Expiry','Settle Price','Number of Contracts','Turnover'],axis=1,inplace=True)
        df.append(stock_fut,ignore_index=True,verify_integrity=False, sort=None)
        print(stock_fut)
        print(stock_fut['Last'].iloc[0])
        
        
        
        d[s] = float(stock_fut['Last'].iloc[0]) * float(stock_fut['Open Interest'].iloc[0]) *size[i]
        i = i + 1
        print(i)
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    print('Dictionary in descending order by value : ',sorted_d)
    df1 = pd.DataFrame({'Name': sorted_d.keys(), 'OI': sorted_d.items()})
    df1.to_csv(r'C:\Users\Admin\Desktop\Finance Python\OI\oiresults.csv')

df = pd.read_csv(r'C:\Users\Admin\Desktop\Finance Python\OI\lotsize.csv')
ls = df.iloc[:,4]
sm = df.iloc[:,2]
sm = sm.drop([0])
sm = list(sm)
sm.pop(0)
sm.pop(0)

ls = ls.drop([0])
rs = map(float,ls)
rs = list(rs)
rs.pop(0)
rs.pop(0)
get_data(sm,rs)
