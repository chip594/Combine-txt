'''

File:           combine_txt.py
Author:         Chip Newman
Date:           01/13/19
Version:        1.0

Description:    This program will read every .txt file within a directory.
                It will store the names in each of those files within a list
                and write those names to a single output file. The program will
                ask the user for a desired output file name, but if one is not 
                provided then a default name will be used.

                The .exe file must be within the same directory as the .txt files.

'''

import os
import pymsgbox

# ensures that the output file will have a name
def add_txt_ext(user_input):
    # runs if the prompt box is empty
    if len(user_input) < 1:
        return '_output'
    # runs if user input is provided
    else:
        return user_input

# ask the user for the desired output file name
user_input = pymsgbox.prompt('Enter the desired name of the output file: (without ".txt")\n ', default=add_txt_ext(''), title='FBPI .txt File Combiner')

# closes program if the user clicks the cancel button
if user_input == None:
    exit(0)

# stores a list of files within the current workign directory
file_list = os.listdir(os.getcwd())

# creates an output file, name is based on user input
output_file = open(add_txt_ext(user_input) + '.txt', 'w')

# creates a list to store the names
names = []

# cycles through every file in the current working directory
for files in file_list:
    # only chooses files that end in .txt
    if files.endswith('.txt'):
        # opens each .txt file and reads line by line
        with open(files, 'r') as f:
            line = f.readline()
            # runs for each line within a file
            while line:
                # removes the return char from a name
                line = line.replace('\n', '')
                # adds the name to the list
                names.append(line)
                # writes the name to the output file
                output_file.write(line)
                # reads the next line
                line = f.readline()
                # writes a return char after each name
                output_file.write('\n')

# closes the output file
output_file.close()