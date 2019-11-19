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
pid = form.getvalue('pid')

sql= """SELECT S.sname, S.address
	FROM suppliers S, catalog C
	WHERE S.sid = C.sid AND C.pid = '%s' AND C.cost = (SELECT max(C.cost)
													   FROM catalog C
													   WHERE C.pid = '%s') """ %(pid,pid)


mycur.execute(sql)

myresult = mycur.fetchall()

print('<h2 align="center">Names and addresses of suppliers who charge the most for the given part</h2>')
print('<table align="center" border><tr><th>Supplier Name</th><th>Supplier Address</th></tr>')
for x in myresult:
	print('<tr><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>')
print('</table>')
