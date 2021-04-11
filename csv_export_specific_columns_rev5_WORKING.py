import pandas as pd
import os
#TODO problem with the files and the for loop but it is working ok
#---------------Directory

#insert the input directory
path = input('Insert folder to CSV files: ')

# Changing the CWD (Current working directory) to path
current_directory = path
os.chdir(current_directory)


#output_directory = input('Insert folder to export mod CSV files: ')

#creating the final directory "mod"  for output if not exists
output_directory = os.path.join(current_directory, r'columns_mod')
if not os.path.exists(output_directory):
   os.makedirs(output_directory)

# select desired columns
       #df = df[['Date', 'Time', 'Corrected Fish X', 'Corrected Fish Y', 'CMG']]
       #Date,Time,Corrected Fish X,Corrected Fish Y,CMG
column_string = input('Enter output columns separated by comma (Be careful, no space between words and no comma in the last column!): ')
       # Be CAREFUL it is not working corrctlly without space between extensions in the input (','). it has to be ('. ')
column_list = column_string.split(",")
# print list

#columns_list.append(columns)
       #headers=input('Insert headers: ')
       #df = df[['headers']]



#Loop for all the csv files in folder.
for root, directory, files in os.walk(path):
    for file in files:

       # This is to read csv files in folder
       df = pd.read_csv(file, sep=",")
       #this is to remove the etxension part from the filename as it is needed for the output filename_mod
       base = os.path.basename(file) #base is the filename.csv
       os.path.splitext(base)#This splits the filename to ('filename', 'CSV')
       file_no_extension=os.path.splitext(base)[0]#this is to take the first [0] part in the list

       ''''# select desired columns
       #df = df[['Date', 'Time', 'Corrected Fish X', 'Corrected Fish Y', 'CMG']]
       columns_list=[]
       columns = input('when done:')
       # Be CAREFUL it is not working correctly without space between extensions in the input (','). it has to be ('. ')
       columns_list.append(columns)
       #headers=input('Insert headers: ')'''
       #df = pd.DataFrame(column_list)
       df = df[column_list]
       print(df)

       #df = DataFrame(column_list).transpose()
       #df = df[columns_list]

       # write to the file (tab separated if sep='t'). "_mod.csv is added to name
       #file_no_extension instead of file is used in order not to have the extension
       #df.to_csv(final_directory + '/' + file_no_extension+"_mod.CSV",sep=',', index=False)
       #if file in directory:
       df.to_csv(output_directory + '//' + file_no_extension+"_columns_mod.CSV", sep=',', index=False)
       #df.to_csv(r'E:\OneDrive\19_Python_Scripts\Personal\test_directory\CSV\mod' + '//' + file_no_extension + "_mod.CSV", sep=',', index=False)
print(df)
print(columns_list)
#print(root)
#print('---',directory)
#print(root)
#TODO there are some errors with the export folder. The for loop output folder need to be
# changed or go back to rev3_WORKING and try to move the _mod files to different output folder


'''
# this assumes that your file is comma separated
# if it is e.g. tab separated you should use pd.read_csv('data.csv', sep = '\t')
# if to include subdirectories

csv_input = input("csv_file: ")
df = pd.read_csv(csv_input, sep=",")

# select desired columns
df = df[['Date', 'Ping']]

#write to the file (tab separated)
df.to_csv('MYFILEnew3.csv', sep=',', index=False)'''



#TODO check why below is not working
'''from __future__ import absolute_import, division, print_function
import csv
from itertools import imap
from operator import itemgetter


def main():
    delimiter = ','
    with open('input.csv', 'rb') as input_file:
        reader = csv.reader(input_file, delimiter=delimiter)
        with open('output.csv', 'wb') as output_file:
            writer = csv.writer(output_file, delimiter=delimiter)
            writer.writerows(imap(itemgetter(0, 5, 4, 7), reader))


if __name__ == '__main__':
    main()
'''


