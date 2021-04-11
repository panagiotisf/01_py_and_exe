#Version 12

# v12 is working. Filenames, filepaths and file number are exported for a specific path
# Changes from previous versions
# The output is saved in user input folder
# option to export specific extensions has been added
# available extensions are shown
# bug if a non existing extension is entered by the user has been addressed by retrieving the file extensions
# option to chose to include sub-folder files to the export
# could be added code to show available extensions and choose from them

#TODO
# mispelled extension in file_extension_string_list



print("\n*** Welcome to 'Filenames and Filepaths'. This script can be used to export .txt files "
      "\ncontaining the file list names and the file list paths. A .txt with the number "
      "of files is also exported.***\n\nPlease send comments and suggestions to: "
      "info@marecho.com or panagiotisf@yahoo.com\n")


''''#Function to Get the current
# working directory
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()'''

#*  *   *   *   *   *   *   *   file paths

#Need to use the following line if current directory is used
#path = (".")
#path = (r'add_path')
path = input('Insert folder to retrieve filenames and filepaths: ')
#path = (r'E:\OneDrive\19_Python_Scripts')
import os


# Printing CWD before  (current working directory)
#print(os.getcwd())

# Changing the CWD
#output_dir = input('Insert output folder:' )
output_dir = path
os.chdir(output_dir)


# Printing CWD after
print('Output folder is:', output_dir)



#lists
files_with_paths = []
files = []
file_extension_list = []
file_list_all = ['all', 'ALL', 'All']
extension_check = []
unique_extension = []
file_extension_variable = None

#*  *   *   *   *   *   *   *   include sub-directories

#inlude subdirectories option
include_subdirectories = None

#Subdirectories_user_answer= input('Do you want to include files in subdirectories? Enter yes or no: ')
answer_list_yes = ['yes', 'Yes', 'YES', 'Y', 'y']
answer_list_no =  ['no', 'No', 'NO', "N", 'n']
active_yes_no = True
while True:
    Subdirectories_user_answer = input("Do you want to include files in subdirectories? Enter yes or no: ")
    if Subdirectories_user_answer in answer_list_yes:
        include_subdirectories = True
        #print('yes')
        active_yes_no = False
        break
    elif Subdirectories_user_answer in answer_list_no:
        include_subdirectories = False
        #print('no')
        active_yes_no = False
        break
    else:
        print("Please enter yes or no.")
#print(include_subdirectories)

#Used to show the existing file types within the folder. List contains duplicated values.
#Transforming to set de-duplicates but without order. Then set is transformed to list again
for r, d, f in os.walk(path, topdown=True):
    for file in f:
        if include_subdirectories == True:
            found_name, found_extension = os.path.splitext(file)
            truncated_extension = found_extension[1:]
            extension_check.append(truncated_extension)
        else:
            d.clear()
            found_name, found_extension = os.path.splitext(file)
            truncated_extension = found_extension[1:]
            extension_check.append(truncated_extension)
    #print(extension_check)
set_extension_check = set(extension_check)
unique_extension = list(set_extension_check)
#print(unique_extension)

'''    elif file_extension not in unique_extension:
        print('this file is not included')'''

#*  *   *   *   *   *   *   *   all or specific file extension check
'''file_extension = input('\n--> For all the files insert all. \n--> For specific file types insert file extensions (without the dot) separated by comma(,)  \n    and hit enter when done: ')
#Be CAREFUL it is not working corrctlly without space between extensions in the input (','). it has to be ('. ')
file_extension_string_list = file_extension.split(', ')
print(file_extension_string_list)'''



active_extension = True
while active_extension == True:
    file_extension = input('\n--> ++++For all the files insert all. \n--> For specific file types insert file extensions (without the dot) separated by comma(,) (Be careful, no space between words!)\n    and hit enter when done: ')
    # Be CAREFUL it is not working corrctlly without space between extensions in the input (','). it has to be ('. ')
    file_extension_string_list = file_extension.split(',')
    common_extensions = [x for x in unique_extension if x in file_extension_string_list]
    if file_extension in file_list_all:
        file_extension_variable = 'all'
        active_extension = False
        break
    elif file_extension not in file_list_all: #TODO mispelled extension in file_extension_string_list
        for i in common_extensions:
            file_extension_variable = 'specific_extensions'
            active_extension = False
            print('unique', unique_extension)
            print('common', common_extensions)
            break
    elif file_extension not in unique_extension:
        print('---------This file type is not found in the input folder. Please try one of the following types: ' + str(unique_extension))
        # file_extension = input('\n--> For all the files insert all. \n--> For specific file types insert file extensions (without the dot) separated by comma(,) \n    and hit enter hwne done: ')
        continue




#===================================================


        #print('Please try again')
#print(file_extension_list)

'''file_extension = "." + input('file type (all or specific file type: ')
if file_extension == "all"'''


#if file_extension ==""

# r=root, d=directories, f = files

# if to include subdirectories
for r, d, f in os.walk(path):
    for file in f:
        if include_subdirectories == True:
            #if file.endswith(('.py', '.jpeg', '.mp4')):
            #if file.endswith(file_extension):
            #if file_extension !='all' in file:
            if file_extension_variable == "specific_extensions":
                for extension in common_extensions:
                    if file.endswith(extension):
                        files_with_paths.append(os.path.join(r, file))
                        files.append(file)
                        file_number = str(len(files))

            else:
                files_with_paths.append(os.path.join(r, file))
                files.append(file)
                file_number = str(len(files))
                #file_number = str(len(files))'''

 # if to exclude subdirectories
        if include_subdirectories == False:
            #if file.endswith(('.py', '.jpeg', '.mp4')):
            #if file.endswith(file_extension):
            #if file_extension !='all' in file:
            d.clear()
            #if file_extension not in file_list_all:
            if file_extension_variable == "specific_extensions":
                for extension in common_extensions:
                    if file.endswith(extension):
                        files_with_paths.append(os.path.join(r, file))
                        files.append(file)
                        file_number = str(len(files))

            else:
                files_with_paths.append(os.path.join(r, file))
                files.append(file)
                file_number = str(len(files))
                #file_number = str(len(files))'''

# bellow need to be modified but kept as bkp
'''
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        #if file.endswith(('.py', '.jpeg', '.mp4')):
        if file.endswith(file_extension):
        #if file_extension !='all' in file:
            files_with_paths.append(os.path.join(r, file))
            files.append(file)
            file_number = str(len(files))
        #else:
            files_with_paths.append(os.path.join(r, file))
            files.append(file)
            #file_number = str(len(files))'''

#below if needed to just show the results
'''for fwp in files_with_paths:
    print(fwp)
for f in files:
    print(f)'''


with open("filenames.txt", "w") as out:
    for filename in files:
        #print(filename)
        out.write(filename+'\n')

with open("filenames_with_paths.txt", "w") as out_paths:
    for filenamepath in files_with_paths:
        #print(filenamepath)
        out_paths.write(filenamepath+'\n')

with open('filenames_number_is_%s.txt'% file_number, "w") as out_no:
    print("The number of files is: " +file_number)
    out_no.write(file_number+'\n')


print("unique_extension"+str(unique_extension))
print("file_extension_string_list"+str(file_extension_string_list))
