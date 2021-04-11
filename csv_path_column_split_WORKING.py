# importing pandas module
import pandas as pd
import os

# reading csv file
csv_input = r'E:\OneDrive\19_Python_Scripts\Personal\test_directory\2021_Cyprus_Vassiliko-Report.CSV'

# Only reads 'File Name'
#df = pd.read_csv(csv_input, usecols = ['File Name'], header = 1)

# Only reads column 1 and buypass header
df= pd.read_csv(csv_input, usecols = [1], header = 0)
df1 = df.iloc[:, 0]
df2= df1.str.split('\\', n = 0,  expand = True).rename(columns = lambda x: "string"+str(x+1))
#df2=df['File Name'].split('\\', expand=True).rename(columns = lambda x: "string"+str(x+1))


#df=df.rename(columns = {'File Name':'new_name'}) #TODO this rename is working!!!! WHY?
df3=df2.rename(columns = {'string7':'File Name'}) #TODO this rename is working
df4= df3.iloc[:, -1]


df.to_csv('MYFILEnew0.csv', sep=',', index=False)
df1.to_csv('MYFILEnew1.csv', sep=',', index=False)
df2.to_csv('MYFILEnew2.csv', sep=',', index=False)
df3.to_csv('MYFILEnew3.csv', sep=',', index=False)
df4.to_csv('MYFILEnew4.csv', sep=',', index=False)
# df display
print(df)
print(df1)
print(df2)
print('-----------df3')
print(df3)
print('**********df4')
print(df4)
#print(df1)
