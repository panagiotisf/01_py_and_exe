'''Step 1: Import packages and set the working directory
Change “/mydir” to your desired working directory'''

import os
import glob
import pandas as pd

#insert the input directory
path = input('Insert folder to CSV files: ')

# Changing the CWD to path
current_directory = path
os.chdir(current_directory)


'''Step 2: Use glob to match the pattern ‘csv’
Match the pattern (‘csv’) and save the list of file names in the ‘all_filenames’ variable. You can check out this link to learn more about regular expression matching.'''

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


'''Step 3: Combine all files in the list and export as CSV
Use pandas to concatenate all files in the list and export as CSV. The output file is named “combined_csv.csv” located in your working directory.'''

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
merged_output_file = input('Insert merged file name: ')
combined_csv.to_csv(merged_output_file+".csv", index=False, encoding='utf-8-sig')

'''encoding = ‘utf-8-sig’ is added to overcome the issue when exporting ‘Non-English’ languages.

#And…it’s done!'''