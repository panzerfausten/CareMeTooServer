class Helper:
	def __init__(self):
		pass
	def listToGrid(self,_list):
		_grid = ""
		for _l in _list:
			_header = "<table>\n<thead>\n<tr>"
			_thead = "<tr>%s</tr>"
			_th = self.generateRowNames(len(_l))
			_thead = _thead % (_th)
			_tr = "</thead><tbody><tr>%s</tr>"

			_grid += _header + _thead
			_data = ""
			for _d in _l:
				print _d
				_td = "<td>%s</td>" %( str(_d))
				_data += _td
			_tr = _tr % (_data)
			_grid += _tr
			#_grid += _data
			_foot = "</tbody></table>"
			_grid += _foot
	
		return _grid
	def generateRowNames(self,_n):
		_res = ""
		for _i in range(0,_n):
			_res += "<th>s%i</th>" % (_i)
		return _res
if __name__ == "__main__":
	h = Helper()
	p = h.listToGrid([[1,2,3],[4,5,6]])
	print p
