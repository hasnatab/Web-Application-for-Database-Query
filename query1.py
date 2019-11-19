#!/usr/bin/python
import mysql.connector
import cgi


mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Terrmairebapp_1",
	database = "SupplyDB" #delete this before creating the database and use after creating for everything else
	)

#create cursor
mycur = mydb.cursor()


print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()
name = form.getvalue('fname')


sql1 = """SELECT S.sid, S.sname, S.address, C.cost
		 FROM Suppliers S, Parts P, Catalog C
		 WHERE S.sid = C.sid AND P.pid = C.pid AND P.pname = '%s' """ %(name)


mycur.execute(sql1)

myresult = mycur.fetchall()

print('<h3 align="center">Supplier information and part cost for a given part name</h3>')
print('<table align="center" border><tr><th>Supplier ID</th><th>Supplier Name</th><th>Supplier Address</th><th>Item ($)</th></tr>')
for x in myresult:
	print('<tr><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td><td>'+str(x[2])+'</td><td>'+str(x[3])+'</td></tr>')
print('</table>')
