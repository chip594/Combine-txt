# combine_txt.py

import os
import pymsgbox

def add_txt_ext(user_input):
    if len(user_input) < 1:
        return '_output'
    else:
        return user_input

user_input = pymsgbox.prompt('Enter the name of the output file:\n (if blank will default to "_output.txt")')
if user_input == None:
    exit(0)

file_list = os.listdir(os.getcwd())

output_file = open((add_txt_ext(user_input) + '.txt'), 'w')

names = []

for files in file_list:
    if files.endswith('.txt'):
        with open(files, 'r') as f:
            line = f.readline()
            while line:
                line = line.replace('\n', '')
                names.append(line)
                output_file.write(line)
                line = f.readline()
                output_file.write('\n')

output_file.close()