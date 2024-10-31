import os
from pathlib import Path
import glob
#file handling and os interaction is the ability of a python script to work with files and interact with the underlaying operating system to perform various tasks. It provides us with libraries, modules etc to help us with file handling.
#one of the advantage of file handling is that it is versatile, it is flexible, it is cross-platform
#disadvantages in python:it can be slow when you are dealing with a large dataset, security risks, it is prone to error, it is very complex when working with advanced file format
# os interacts with the underlaying operating system to persom system level operation e.g managing files and diectoties, executing system commands and querying system information.


# myfile = open('note.txt', 'r')
# print(myfile.read())
# myfile.close()

# myfile = open(r'C:\Users\hp\Documents\filehandlingexample.txt', 'r')
# print(myfile.read())
# myfile.close()

# with open(r'C:\Users\hp\Documents\filehandlingexample.txt', 'r') as file:
#     content = file.read()
#     print(content)

#file mode
'''
r - read only
w - write
w+ - write
a - append
x -create
'''

# with open('testing.txt', 'w') as file:
#     content = file.write('the content in this file has been erased')
#     print('job done')

# with open('testing.txt', 'a') as file:
#     content = file.write(' i am just adding more texts to the file')
#     print('job done')
    # content= file.read()

# with open('example.txt', 'w') as file:
#     file.write("a new file")
#     print(file)

# with open(r"C:\Users\hp\Documents\example.pdf", 'w') as file:
#     content = file.write('this s new pdf file')
#     print('done')

# from PyPDF2 import PdfReader
# reader = PdfReader(r"C:\Users\hp\Documents\example.pdf")
# number_of_pages = len(reader.pages)
# print(number_of_pages)
# for page in range(len(reader.pages)):
#     page = reader.pages[page]
#     text = page.extract_text()
#     print(text)

# num_of_dir = os.scandir()
# for files in num_of_dir:
#     print('files name:', files)
# print(num_of_dir)

# with os.scandir(r'c:\Users\hp\Desktop\LEVEL 1') as list_dir_content:
#     for files in list_dir_content:
#         print('files name:', files)
# print(type(files))

# list_dir_content = Path()
# for entry in list_dir_content.iterdir():
#     print(entry)
# print(type(entry))

# list_dir_content = Path(r'c:\Users\hp\Desktop\LEVEL 1')
# for entry in list_dir_content.iterdir():
#     print(entry)
# print(type(entry))

# new_dir = os.mkdir('first folder')
# print('done')


# new_dir = os.mkdir(r'C:\Users\hp\Desktop\LEVEL 1\first folder2')
# print('done')

# with open(r'c:\Users\hp\Desktop\LEVEL 1\first folder2\myfile2.txt', 'x', encoding= 'utf-8') as file:
#     content = file.write('creating a new file using the x mode')
#     print(file.read())
#     print('done')

# directory_path = 'folder3'

# if not os.path.exists(directory_path):
#     os.makedirs(directory_path)
#     with open(r'folder3\myfile1', 'w')  as file:
#         file.write('hello')
#         print('text written successfully')
#         print('directory created successfully')
# else:
#     print('directory already exists')

# file_path = os.path.join(r'C:\python-works2', 'example5.py')

# if not os.path.exists(file_path):
#     os.makedirs(file_path)
#     with open(r'file_path', 'w') as file:
#         file.write("this is a py file created with python")
#     print('file created successfully')
# else:
#     print('file already exists')

# print(glob.glob('*.txt'))
# for file in glob.glob('**/*.py', recursive=True):
#     print(file)

# for dirpath, dirnames, files in os.walk('.'):
#     print(f'i am >> {dirnames}')
#     print(f"avalable directory: {dirpath}")
#     for filename in files:
#         print(filename, 'files')
#         print()