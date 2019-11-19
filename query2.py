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
cost = form.getvalue('cost')


sql = """SELECT DISTINCT (S.sname)
		FROM suppliers S, catalog C
		WHERE S.sid = C.sid AND c.cost >= '%s' """ %(cost)

mycur.execute(sql)

myresult = mycur.fetchall()

print('<h2 align="center">Supplier who supplied one or more part/s with cost equal to or more than the given cost</h2>')
print('<table align="center" border><tr><th>Supplier Name</th></tr>')
for x in myresult:
	print('<tr><td>'+str(x[0])+'</td></tr>')
print('</table>')
