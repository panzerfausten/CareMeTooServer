from DbObject import DbObject
class CareGiver(DbObject):
	def __init__(self):
		self.tableName = "caregivers"
	def get(self, _id):
		super.cnx(super._query_getId %(self.caregivers,_id))

c = CareGiver()
c.get(1)
