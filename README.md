# Combine-txt

Combine txt is a program that I wrote for a local company. The company receives hundreds of text files with one or two names in each file. The request was for a solution to speed up the process of having to manually open each file and paste the names into a single text file.

 

How it works!

Combine txt will scan the current directory and open all of the files with the .txt extension. It will print the names from the separate files, line by line into a single file. The program will ask the user for a desired name for the output file, but if none is given then the program will default to _output.txt.

 
Combine txt is written in Python 3.7

The .exe was built using pyinstaller 
    - pyinstaller -F -w combine_txt.py