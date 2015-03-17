class ViewRenderer:
	def __init__(self,viewname):
		self.viewname = viewname
                self.views = { "showCaregivers":"views/caregivers/show.html", "index":"views/main/CareMeTooWeb/public_html/index.html", "ml":"views/ml/index.html"}
		self.renderedView = ""
	def render(self):
		self.fileName = self.views[self.viewname]
		self._file = open(self.fileName,"r")
		if(self._file != None):
			self.renderedView = "".join(self._file.readlines())
			return self.renderedView
		else:
			return "Invalid View"
	def inject(self,tag,code):
		return self.renderedView.replace(tag,code)
#v = ViewRenderer("ml")
#print v.render()
