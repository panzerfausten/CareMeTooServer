from DbObject import DbObject
import json
class CareGiver(DbObject):
	def __init__(self,idcaregivers=-1,name="",username="",password=""):
		DbObject.__init__(self)
		self._tableName = "caregivers"
		self.idcaregivers = idcaregivers
		self.name = name
		self.username= username
		self.password= password
		self._query_getId = "SELECT * FROM %s WHERE idcaregivers=%i;"

	def get(self, _id):
		_getQuery = self._query_getId % ( self._tableName, _id) 
		_cursor =self.cnx.cursor()
		_cursor.execute(_getQuery)
		_c = None
		for idcaregivers,name,username,password in _cursor:
			_c = CareGiver(idcaregivers,name,username,password)
		return _c
	def all(self,toList=False):
		_getQuery = "SELECT * FROM %s;" % (self._tableName)
		_cursor =self.cnx.cursor()
		_cursor.execute(_getQuery)
		_caregivers = []
		for idcaregivers,name,username,password in _cursor:
			_c = CareGiver(idcaregivers,name,username,password)
			if not toList:
				_caregivers.append(_c)
			else:
				_caregivers.append( [str(idcaregivers),name,username,password])

		return _caregivers
	def delete(self,_id):
		_delQuery = "DELETE FROM caregivers where idcaregivers=%i;" % _id
		_cursor =self.cnx.cursor()
		_cursor.execute(_delQuery)
		return self.cnx.commit()
	def insert(self,name="",username="",password=""):
		_insertQuery= "INSERT INTO caregivers (name,username,password) VALUES('%s','%s','%s');"
		_insertQuery= _insertQuery % (name,username,password)
		_cursor =self.cnx.cursor()

		_cursor.execute(_insertQuery)
		self.cnx.commit()
		_lastid = _cursor.lastrowid
		return self.get(_lastid)	
	def toList(self):
		return [str(self.idcaregivers),self.name,self.username,self.password]
	def toJson(self):
		return json.dumps({"name":self.name,"username":self.username,"password":self.password})
if __name__ == "__main__":
    c = CareGiver()

