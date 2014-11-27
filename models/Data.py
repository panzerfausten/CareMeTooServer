from DbObject import DbObject
import json
class Data(DbObject):
	def __init__(self,iddata=-1,idcaregiver="",datatype="",value="", extra="",location="",timestamp=""):
		DbObject.__init__(self)
		self._tableName = "data"
		self.iddata= iddata
		self.idcaregiver= idcaregiver
		self.datatype = datatype
		self.value = value
		self.extra = extra
		self.location = location
		self.timestamp = timestamp
		self._query_getId = "SELECT * FROM %s WHERE iddata=%i and idcaregiver=%i;"
		self._query_getById = "SELECT * FROM %s WHERE iddata=%i"

	def get(self, _id,_idcaregiver):
		_getQuery = self._query_getId % ( self._tableName, _id,_idcaregiver) 
		_cursor =self.cnx.cursor()
		_cursor.execute(_getQuery)
		_d = None
		for iddata,idcaregiver,datatype,value,extra,location,timestamp in _cursor:
			_d = Data(iddata,idcaregiver,datatype,value,extra,location,timestamp)
		return _d
	def getById(self, _id):
		_getQuery = self._query_getById % ( self._tableName, _id) 
		_cursor =self.cnx.cursor()
		_cursor.execute(_getQuery)
		_d = None
		for iddata,idcaregiver,datatype,value,extra,location,timestamp in _cursor:
			_d = Data(iddata,idcaregiver,datatype,value,extra,location,timestamp)
		return _d

	def all(self,_idcaregiver,toList=False):
		_getQuery = "SELECT * FROM %s where idcaregiver=%i;" % (self._tableName,_idcaregiver)
		_cursor =self.cnx.cursor()
		_cursor.execute(_getQuery)
		_datas = []
		for iddata,idcaregiver,datatype,value,extra,location,timestamp in _cursor:
			_d = Data()
			if not toList:
				_datas.append(_d)
			else:
				_datas.append( [str(iddata),str(idcaregiver),datatype,value,extra,location,timestamp])

		return _datas
	def delete(self,_id):
		_delQuery = "DELETE FROM data where iddata=%i;" % _id
		_cursor =self.cnx.cursor()
		_cursor.execute(_delQuery)
		return self.cnx.commit()

	def insert(self,idcaregiver,datatype,value,extra,location,timestamp):
		_insertQuery= "INSERT INTO data (idcaregiver,datatype,value,extra,location,timestamp) VALUES('%i','%s','%s','%s','%s','%s');"
		_insertQuery= _insertQuery % (idcaregiver,datatype,value,extra,location,timestamp)
		_cursor =self.cnx.cursor()

		_cursor.execute(_insertQuery)
		self.cnx.commit()
		_lastid = _cursor.lastrowid
		return self.getById(_lastid)	
	def toList(self):
		return [self.iddata,self.idcaregiver,self.datatype,self.value,self.extra,self.location,self.timestamp]
	def toJson(self):
		return json.dumps({"iddata":self.iddata,"idcaregiver":self.idcaregiver,"datatype":self.datatype,"value":self.value,"extra":self.extra,"location":self.location,"timestamp":self.timestamp.strftime('%Y-%m-%dT%H:%M:%S')})
if __name__ == "__main__":
    d = Data()
    _insertedData  = d.insert(1,"HR","78","listening to the music","10,10","2014-11-27 11:53:00")
    print _insertedData.extra
#print d.getById(102041).extra
#print d.all(1)
#print d.all(toList=True)
#print d.getById(19)
