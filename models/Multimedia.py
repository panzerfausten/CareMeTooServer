from DbObject import DbObject
import json
class Multimedia(DbObject):
	def __init__(self,idmultimedia=-1,idcaregiver=-1,description="",path="",extra=""):
		DbObject.__init__(self)
		self._tableName = "multimedia"
		self.idmultimedia = idmultimedia
		self.idcaregiver = idcaregiver
		self.description = description
		self.path = path
		self.extra = extra
		self._query_getId = "SELECT * FROM %s WHERE idmultimedia=%i;"

	def get(self, _id):
		_getQuery = self._query_getId % ( self._tableName, _id) 
		_cursor =self.cnx.cursor()
		_cursor.execute(_getQuery)
		_m = None
		for idmultimedia,idcaregiver,description,path,extra in _cursor:
			_m = Multimedia(idmultimedia,idcaregiver,description,path,extra)
		return _m
	def all(self,toList=False):
		_getQuery = "SELECT * FROM %s;" % (self._tableName)
		_cursor =self.cnx.cursor()
		_cursor.execute(_getQuery)
		_multimedias = []
		for idmultimedia,idcaregiver,description,path,extra in _cursor:
			_m = CareGiver(idmultimedia,idcaregiver,description,path,extra)
			if not toList:
				_multimedias.append(_m)
			else:
				_multimedias.append( [str(idmultimedia),str(idcaregiver),description,path,extra])

		return _multimedias
	def delete(self,_id):
		_delQuery = "DELETE FROM multimedia where idmultimedia=%i;" % _id
		_cursor =self.cnx.cursor()
		_cursor.execute(_delQuery)
		return self.cnx.commit()
	def insert(self,idcaregiver=-1,description="",path="",extra=""):
		_insertQuery= "INSERT INTO multimedia (idcaregiver,description,path,extra) VALUES('%s','%s','%s','%s');"
		_insertQuery= _insertQuery % (idcaregiver,description,path,extra)
		_cursor =self.cnx.cursor()

		_cursor.execute(_insertQuery)
		self.cnx.commit()
		_lastid = _cursor.lastrowid
		return self.get(_lastid)	
	def toList(self):
		return [str(self.idmultimedia),str(self.idcaregiver),self.description,self.path,self.extra]
	def toJson(self):
		return json.dumps({"idcaregiver":self.idcaregiver,"description":self.description,"path":self.path,"extra":self.extra})
#m = Multimedia()
#m.insert(1,"multimedia test","/asdasd.m4a","adasd")
#idd = m.get(1).idmultimedia
#m.delete(idd)
