from pandas_datareader import data, wb 
import datetime
#using this in order to pull data from internet
import pandas_datareader.data as web
#creating start and end variable. we would need data between these dates
start = datetime.datetime(2010,1, 1)
end = datetime.datetime(2015, 8, 22)


df = web.DataReader("ICICIBANK.NS", "yahoo", start, end)
#prints data frame
print(df)
print(df.head())
