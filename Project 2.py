CRUD operations using mysql database

#create a table

import mysql.connector
mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="dbpython")
mycursor = mysqldb.cursor()
mycursor.execute("create table student(roll INT,name VARCHAR(255), marks INT)")
mysqldb.close()

#read data

import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="dbpython")
mycursor=mysqldb.cursor()
try:
   mycursor.execute("select * from student")
   result=mycursor.fetchall()
   for i in result:
      roll=i[0]
      name=i[1]
      marks=i[2]
      print(roll,name,marks)
except:
   print('Error:Unable to fetch data.')
mysqldb.close()


#update data

ollowing code uses an UPDATE SQL query to update an existing record.

import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="dbpython")
mycursor=mysqldb.cursor()
try:
   mycursor.execute("UPDATE student SET name='Ramu', marks=100 WHERE roll=1")
   mysqldb.commit()
   print('Record updated successfully...')
except:
   mysqldb.rollback()
mysqldb.close()

#delete data

import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="dbpython")
mycursor=mysqldb.cursor()
try:
   mycursor.execute("DELETE FROM student WHERE roll=2")
   mysqldb.commit()
   print('Record deteted successfully...')
except:
   mysqldb.rollback()
mysqldb.close()