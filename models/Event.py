from DbObject import DbObject
import Multimedia
import json
class Event(DbObject):
	def __init__(self,idevent= -1, idcaregiver=-1, idmultimedia=-1, activity="",mood="",description="",timestamp=""):
		DbObject.__init__(self)
		self._tableName = "event"
		self.idevent = idevent
		self.idcaregiver = idcaregiver
		self.idmultimedia = idmultimedia
		self.activity = activity
		self.mood = mood
		self.description = description
		self.timestamp = timestamp
		self._query_getId = "SELECT * FROM %s WHERE idevent=%i;"

	def get(self, _id):
		_getQuery = self._query_getId % ( self._tableName, _id) 
		_cursor =self.cnx.cursor()
		_cursor.execute(_getQuery)
		_e = None
		for idevent,idcaregiver,idmultimedia,activity,mood,description,timestamp in _cursor:
			_e = Event(idevent,idcaregiver,idmultimedia,activity,mood,description,timestamp)
		return _e
	def all(self,idcaregiver=-1,toList=False,toJson=False):
		_getQuery = "SELECT * FROM %s where idcaregiver= %i;" % (self._tableName,idcaregiver)
		_cursor =self.cnx.cursor()
		_cursor.execute(_getQuery)
		_events = []
		for idevent,idcaregiver,idmultimedia,activity,mood,description,timestamp in _cursor:
			_e = Event(idevent,idcaregiver,idmultimedia,activity,mood,description,timestamp)
			if toList:
				_events.append([str(idevent),str(idcaregiver),str(idmultimedia),activity,mood,description,timestamp])
			elif toJson:
				_events.append(_e)
		if toList:
			return _events
		elif toJson:
			_dict_events = []
			for _e in _events:
				_dict_events.append(_e.toDict())
			return json.dumps(_dict_events)
		return _events
	def delete(self,_id):
		_delQuery = "DELETE FROM %s where idevent=%i;" % (self._tableName,_id)
		_cursor =self.cnx.cursor()
		_cursor.execute(_delQuery)
		return self.cnx.commit()
	def insert(self,idevent=-1,idcaregiver=-1,idmultimedia=-1,activity='',mood='',description='',timestamp=''):
		_insertQuery= "INSERT INTO %s (idcaregiver,idmultimedia,activity,mood,description,timestamp) VALUES('%s','%s','%s','%s','%s','%s');"
		_insertQuery= _insertQuery % (self._tableName,idcaregiver,idmultimedia,activity,mood,description,timestamp)
		_cursor =self.cnx.cursor()

		_cursor.execute(_insertQuery)
		self.cnx.commit()
		_lastid = _cursor.lastrowid
		return self.get(_lastid)	
	def toList(self):
		return [str(idevent),str(idcaregiver),str(idmultimedia),activity,mood,description,timestamp]
	def toJson(self):
		if (self.idmultimedia != -1):
			
			_M = Multimedia.Multimedia()
			_m = _M.get(self.idmultimedia)
			return json.dumps({"activity":self.activity,"mood":self.mood,"description":self.description,"timestamp":self.timestamp.strftime('%Y-%m-%dT%H:%M:%S'), "multimedia":_m.toDict() })
		else:
			return json.dumps({"activity":self.activity,"mood":self.mood,"description":self.description,"timestamp":self.timestamp.strftime('%Y-%m-%dT%H:%M:%S')})

	def toDict(self):
		_hasMultimedia = True
		try:
			int (self.idmultimedia)
		except:
			_hasMultimedia = False
		if (_hasMultimedia ):
			_M = Multimedia.Multimedia()
			_m = _M.get(self.idmultimedia)
		
			return {"activity":self.activity,"mood":self.mood,"description":self.description,"timestamp":self.timestamp.strftime('%Y-%m-%dT%H:%M:%S'), "multimedia":_m.toDict() }
		else:
			return {"activity":self.activity,"mood":self.mood,"description":self.description,"timestamp":self.timestamp.strftime('%Y-%m-%dT%H:%M:%S')}


c = Event()
print c.get(49).toJson()
