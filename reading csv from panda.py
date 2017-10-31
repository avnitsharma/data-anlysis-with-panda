import pandas as pd

df= pd.read_csv('IBM.csv')
df.set_index('Timestamp',inplace=True)
df.rename(columns={'Ticker':'Company'}, inplace=True)

'''we can save this as a new data set by using 
df.to_csv('new.csv') '''

#we can perform various action like  removing header,renaming or adding them
#df.to_csv('IBM.csv', header=False)

print(df)
