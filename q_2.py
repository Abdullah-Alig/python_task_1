# 2. Provide a program to read the CSV file.
# • CSV file has three columns, the first column names, the second column is birthdate(YYYYMM-DD) the third column is salary.
# • Read the file and display the data and age in the terminal.
# • The file path, delimiter, and quote char are the input by the user.
# • The program has to work from the terminal. The input and output have been taken/displayed
# on the terminal.

import pandas as pd
from datetime import datetime, date

# file = "C:/Users/BizzAppDev/hello.csv"
file = input("Enter CSV file full path: ")
delimiter = input("Enter delimiter: ")
# print(delimiter)
quotechar = input("Enter quotechar: ")
name = []
birthdate = []
salary = []
age = []
columns = ["names","birthdate","salary"]
with open(file, newline='') as csvfile:
    spamreader = pd.read_csv(csvfile, delimiter=delimiter, quotechar=quotechar, usecols=columns, engine='python')
    # spamreader = pd.read_csv(csvfile, delimiter='\t', quotechar='|', usecols=columns, engine='python')
    name.append(spamreader['names'].tolist())
    birthdate.append(spamreader['birthdate'].tolist())
    salary.append(spamreader['salary'].tolist())
    bornall = spamreader['birthdate']
    len = len(bornall)
    for i in range(0, len):
        born = datetime.strptime(bornall[i], "%d-%m-%Y").date()
        today = date.today()
        age.append(str(today.year - born.year - ((today.month,today.day) < (born.month,born.day)))+' Years')

print("Name : ",name)
print("Birth Date : ",birthdate)
print("Salary : ",salary)
print("Age : ",age)

