#Rename files of a folder using input and output filename parts
print("\n--- Welcome to 'file renamer'. This script can be used to rename multiple files in a directory ---"      
      "\nPlease send comments and suggestions to: "
      "info@marecho.com or panagiotisf@yahoo.com\n")

import os

path = input('Insert folder rename files: ')
old_filename_part = input('Insert old filename part: ')
new_filename_part = input('Insert new filename part: ')

for root, directory, files in os.walk(path):
    for file in files:
        os.chdir(path)
        if file.startswith(old_filename_part):
            os.rename(file, file.replace(old_filename_part, new_filename_part))
