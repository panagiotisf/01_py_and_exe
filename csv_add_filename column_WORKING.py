import pandas as pd
import os

#---------------Directory

#insert the input directory
path = input('Insert folder to CSV files: ')

# Changing the CWD (Current working directory) to path
current_directory = path
os.chdir(current_directory)

#creating the final directory "mod"  for output if not exists
output_directory = os.path.join(current_directory, r'filename_column_appended')
if not os.path.exists(output_directory):
   os.makedirs(output_directory)



#Loop for all the csv files in folder.

data = []
file_extension_question = input('Do you want to include file extension? (y/n): ')
for root, directory, files in os.walk(path):
    for file in files:
       # This is to read csv files in folder
       df = pd.read_csv(file, sep=",")
       #this is to remove the etxension part from the filename as it is needed for the output filename_mod
       base = os.path.basename(file) #base is the filename.csv
       os.path.splitext(base)#This splits the filename to ('filename', 'CSV')
       file_no_extension=os.path.splitext(base)[0]#this is to take the first [0] part in the list

       if file_extension_question =="y":
         # append filename in csv (last column
         df['filename'] = os.path.basename(file)
         data.append(df)
       elif file_extension_question =="n":
         # append filename in csv (last column
         df['filename'] = os.path.basename(file_no_extension)
         data.append(df)
         #if filename need to be in the first column insert should be used? #TODO check code for that
          #data.insert(df:)


       # write to the file (tab separated). "_mod.csv is added to name
       #file_no_extension instead of file is used in order not to have the extension
       #df.to_csv(file_no_extension+"_mod.CSV",sep=',', index=False)
       df.to_csv(output_directory + '//' + file_no_extension + "_filename.CSV", sep=',', index=False)
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