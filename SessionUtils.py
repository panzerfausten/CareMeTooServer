from sklearn import preprocessing
class SessionUtils:
	def __init__(self,session):
		self.session = session
	def segmentateData(self,data,n=20):
		_x = 0
		_segments = []
		_segment = []
		for _e, _d in enumerate(data):
			if( _x < n):
				_segment.append(_d)
			else:
				_x = -1
				_segments.append(_segment)
				_segment = []

			"""if(_e == (len(data) -1)):
				_segments.append(_segment)
			"""
			_x += 1
		return _segments
        def normalize(self,data):
                _data_to_norm = np.asarray(data)
                min_max_scaler = preprocessing.MinMaxScaler()
                _data_normalized = min_max_scaler.fit_transform(_data_to_norm)
                return _data_normalized
	def removeNones(self,data):
		_g_noNones = []
		for _g in data:
			if (_g != None):
				_g_noNones.append(_g)

		return _g_noNones
