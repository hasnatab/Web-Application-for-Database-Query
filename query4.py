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
color = form.getvalue('color')
address = form.getvalue('address')

sql4= """SELECT DISTINCT(P.pname)
		 FROM Suppliers S, Catalog C, Parts P
		 WHERE S.sid = C.sid AND C.pid = P.pid and S.address = '%s' and p.color = '%s' """ %(address,color)


mycur.execute(sql4)

myresult = mycur.fetchall()

print('<h2 align="center">Name of parts with the given color which are supplied by suppliers with given address</h2>')
print('<table align="center" border><tr><th>Parts Name</th></tr>')
for x in myresult:
	print('<tr><td>'+str(x[0])+'</td></tr>')
print('</table>')
