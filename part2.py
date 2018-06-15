# these should be the only imports you need
import sys
import sqlite3 as sqlite

conn = sqlite.connect('Northwind_small.sqlite')
cur = conn.cursor()

# usage should be 
command = sys.argv[1]


#  python3 part2.py customers

if command == "customers":

	statement1 = "SELECT Id, ContactName "
	statement1 += "FROM customer;"



	print("Id    | Customer Name")



	rows_in_customer_table = cur.execute(statement1)
	for row in rows_in_customer_table:
		(ID, CustomerName) = row;
		print ("%s | %s"%(ID, CustomerName))

#  python3 part2.py employees
elif command == "employees":



	statement2 = "SELECT Id, FirstName, LastName "
	statement2 += "FROM employee;"



	print("Id | Employee Name")


	rows_in_employee_table = cur.execute(statement2)
	for row in rows_in_employee_table:
		(ID, FirstName, LastName) = row;
		print ("%s  | %s %s"% (ID, FirstName, LastName))


elif command == "orders":
	option2 = sys.argv[2]    #  python3 part2.py orders cust=<customer id>
	
	command2, option3 = option2.split('=')

	if command2 == "cust":
			
		statement3 = "SELECT OrderDate "
		statement3 += "FROM [Order] "
		statement3 += "WHERE CustomerId = '%s' " %  option3  ;

		
		print ("Order Dates")

		orderdate_by_id = cur.execute(statement3)
		for row in orderdate_by_id:
			OrderDate = row[0];
			print (OrderDate)


#  python3 part2.py orders emp=<employee last name>

	

	if command2 == "emp":

		empLastName = option3
			
		statement4 = "SELECT OrderDate "
		statement4 += "FROM [Order] "
		statement4 += "WHERE EmployeeId = (SELECT EmployeeId FROM Employee WHERE LastName = '%s')" % empLastName ;
		
		print ("Order Dates")

		orderdate_by_id = cur.execute(statement4)
		for row in orderdate_by_id:
			OrderDate = row[0];
			print (OrderDate)		


















