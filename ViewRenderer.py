class ViewRenderer:
	def __init__(self,viewname):
		self.viewname = viewname
                self.views = { "showCaregivers":"views/caregivers/show.html", "index":"views/main/CareMeTooWeb/public_html/index.html"}
	def render(self):
		self.fileName = self.views[self.viewname]
		self._file = open(self.fileName,"r")
		if(self._file != None):
			return "".join(self._file.readlines())
		else:
			return "Invalid View"

#v = ViewRenderer("showUsers")
#print v.render()
