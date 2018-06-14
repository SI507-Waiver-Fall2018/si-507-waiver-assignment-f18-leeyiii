# these should be the only imports you need
import sys
import sqlite3 as sqlite

conn = sqlite.connect('Northwind_small.sqlite')
cur = conn.cursor()

# usage should be 
command = sys.argv[1]


#  python3 part2.py customers

if command == "customer":

	statement1 = "SELECT Id, ContactName "
	statement1 += "FROM %s" % command ;



	print("Customer Table")


	rows_in_customer_table = cur.execute(statement1)
	for row in rows_in_customer_table:
		(ID, CustomerName) = row;
		print ("%s | %s"%(ID, CustomerName))

#  python3 part2.py employees
elif command == "employee":



	statement2 = "SELECT Id, FirstName, LastName "
	statement2 += "FROM %s" % command ;



	print("Employee Table")


	rows_in_employee_table = cur.execute(statement2)
	for row in rows_in_employee_table:
		(ID, FirstName, LastName) = row;
		print (ID, FirstName, LastName)


elif command == "order":

#  python3 part2.py orders cust=<customer id>
	command2 = sys.argv[2]
	if command2[:4] == "cust":
		#todo
	

	

#  python3 part2.py orders emp=<employee last name>
	elif command2[:3] == "emp":
		#todo







