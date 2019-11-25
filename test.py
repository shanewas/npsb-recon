import pandas as pd

loc = (r"resources/pandas_simple.xlsx")
df = pd.read_excel (loc)
 #for an earlier version of Excel, you may need to use the file extension of 'xls'
print (df)
