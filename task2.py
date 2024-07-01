import pandas as pd
df = pd.read_csv('01.Data Cleaning and Preprocessing.csv') # loading csv file
#print(df.to_string()) #printing whole csv file
#df_filtered = df[(df['ChipRate'] > 15.00) & (df['BlowFlow'] > 1200.00)] # printing data using condition
#print(df_filtered)
#df_filtered.to_csv('C:\python projects\filtered data.csv', index= False ) data to csv file
print(df.isnull()) #.sum() for number of empty entries
df.fillna(0, inplace=True) # dropna(), interpolate()
df.to_csv('new file.csv', index=False)
summary = df.describe() # calculating summary statistics
print(summary)