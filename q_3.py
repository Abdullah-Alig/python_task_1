# 3. Provide a program to create tables (Employee, Department,
# Project) in database Sqlite and insert the data.
# • Make sure to add basic field, with employee to department and project relation.
# • Make sure maintain M2M relation between employee and project. 

from ast import Assign
import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# # Add department start here
departmentDetails = 'create table if not exists departmentdetails(id INTEGER PRIMARY KEY AUTOINCREMENT,departmentName VARCHAR(100) NOT NULL)'
c.execute(departmentDetails)

departmentName = input("Enter Department Name : ")
data_department = (departmentName,)
sql_department = ''' INSERT INTO departmentdetails(departmentName) VALUES(?) '''
c.execute(sql_department,data_department)
conn.commit()
departmentId = c.lastrowid
print("Department Added Successfully ")
# # Add department end here

# # Add employee start here
employee_details = 'create table if not exists employee_details(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(100) NOT NULL,email VARCHAR(100) NOT NULL,departmentId int NOT NULL)'
c.execute(employee_details)

name = input("Enter Employee Name : ")
email = input("Enter Employee Email id : ")
data_employee = (name,email,departmentId)
sql_emplouyee = ''' INSERT INTO employee_details(name,email,departmentId) VALUES(?,?,?) '''
c.execute(sql_emplouyee,data_employee)
conn.commit()
empId = c.lastrowid
print("Employee Added Successfully ")

# # Add employee end here

# # Add project start here
project_details = 'create table if not exists project_details(id INTEGER PRIMARY KEY AUTOINCREMENT,projectName VARCHAR(100) NOT NULL)'
c.execute(project_details)

projectName = input("Enter Project Name : ")
data_project = (projectName,)
sql_project = ''' INSERT INTO project_details(projectName) VALUES(?) '''
c.execute(sql_project,data_project)
conn.commit()
projectId = c.lastrowid
print("Project Added Successfully ")
# Add department end here

sql_get_employee_data = ''' SELECT * FROM employee_details'''
c.execute(sql_get_employee_data)
conn.commit()
setEmplyeeId = input("Enter Employee id from above row : ")

sql_get_project_data = ''' SELECT * FROM project_details'''
c.execute(sql_get_project_data)
conn.commit()
setProjectId = input("Enter Project id from above row : ")

# Assign project to employee here start here
assign_employee_project = 'create table if not exists assign_employee_project(id INTEGER PRIMARY KEY AUTOINCREMENT,employeeId int NOT NULL,projectId int NOT NULL)'
c.execute(assign_employee_project)

assing_project_data = (setEmplyeeId,setProjectId)
sql_assing_project = ''' INSERT INTO assign_employee_project(employeeId,projectId) VALUES(?,?) '''
c.execute(sql_assing_project,assing_project_data)
conn.commit()
print("Project assign Successfully ")

# Assign project to employee here end here


