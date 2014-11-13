import mysql.connector
class DbObject:
	def __init__(self):
		self.cnx = mysql.connector.connect(user='root', password='',
				host='127.0.0.1',database='CareMeToo')
		self._query_getId = "SELECT * FROM %s WHERE ID=%i"
		#cnx.close()
