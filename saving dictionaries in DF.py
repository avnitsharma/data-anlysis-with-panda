import pandas as pd

###we can turn this dictionarie into a excel Dataframe
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

avnit =  {'Boom':[3,2,3,4,5,6,546],
         'Ramu' : [54,554,4,545,454,487,7],
         'Shamu' : [545,56,8,45,8,45,84]}

#putting the dictionary into the dataframe
df = pd.DataFrame(web_stats)
#setting up new index
df.set_index('Day', inplace=True)
print (df.head())
#using head will give top entries where as tail will give end entries
df = pd.DataFrame(avnit)
print (df.head())
