# combine_txt.py

import kivy
kivy.require('1.9.0')

from kivy.core.window import Window
Window.size = (350, 150)

import os
from os.path import abspath, relpath
from pathlib import Path
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

output_file = open('output.txt', 'w')

path = ('\\src\\input-dir\\')
full_path = (os.getcwd() + path)
file_list = os.listdir(full_path)

names = []
tempNames = []

for files in file_list:
    if files.endswith('.txt'):
        with open(full_path + files, 'r') as f:
            line = f.readline()
            while line:
                line = line.replace('\n', '')
                names.append(line)
                output_file.write(line)
                line = f.readline()
                output_file.write('\n')

class Combine_txt_GridLayout(GridLayout):
    pass

class Combine_txtApp(App):
    def build(self):
        self.title = 'FBPI .txt Combiner'
        return Combine_txt_GridLayout()

ct_app = Combine_txtApp()
ct_app.run()

output_file.close()