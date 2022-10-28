# 4 Provide a program to read the file from URL and display the content
# in terminal.
# • The file URL has to be input by the user.
# • The program has to work from the terminal. The input and output have been taken/displayed
# on the terminal.

import requests
file_url = 'https://filesamples.com/samples/document/txt/sample3.txt'

# file_url = input("Enter CSV file url: ")
response = requests.get(file_url)

if (response.status_code):
    data = response.text
    for line in enumerate(data.split('\n')):
        print(line)