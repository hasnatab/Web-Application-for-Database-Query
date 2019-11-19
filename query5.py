#!/usr/bin/python
import mysql.connector
import cgi


mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Terrmairebapp_1",
	database = "SupplyDB"
	)

#create cursor
mycur = mydb.cursor()


print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()
address = form.getvalue('address')

sql5= """
		SELECT S.sid, S.sname
		FROM Suppliers S
		WHERE S.address = '%s' AND S.sid NOT IN

			(SELECT  S1.sid
			FROM Suppliers S1, Catalog C1
			WHERE S1.sid = C1.sid AND S1.address = '%s')""" %(address,address)


mycur.execute(sql5)

myresult = mycur.fetchall()

print('<h2 align="center">IDs and names of Suppliers who do not supply any part in the given address</h2>')
print('<table align="center" border><tr><th>Supplier ID</th><th>Supplier Name</th></tr>')
for x in myresult:
	print('<tr><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>')
print('</table>')
