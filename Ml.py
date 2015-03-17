from maxi import session
from SessionUtils import SessionUtils
##############################MACHINE LEARNING
from sklearn import svm
from sklearn import cross_validation
import numpy as np

class Ml:
	def __init__(self,file_a,file_b,file_c):
		####open session files
		self.s_sample = session(file_a)
		self._grouped_sample = self.s_sample.groupBySec(self.s_sample._dataGSR,True,False)

		self.s_t1 = session(file_b)
		self._grouped_t1 = self.s_t1.groupBySec(self.s_t1._dataGSR,True,False)

		self.s_t2 = session(file_c)
		self._grouped_t2 = self.s_t2.groupBySec(self.s_t2._dataGSR,True,False)
		##### NORMALIZE AND THEN SEGMENTATE SAMPLE
		_su = SessionUtils(self.s_sample)
		self._g_noNones_sample = _su.removeNones(self._grouped_sample)
		self._normalized_sample  = self.s_sample.normalize(self._g_noNones_sample)
		self._segments_sample = _su.segmentateData(self._normalized_sample)
		##### NORMALIZE AND THEN SEGMENTATE T1
		_su = SessionUtils(self.s_t1)
		self._g_noNones_t1 =  _su.removeNones(self._grouped_t1)
		self._normalized_t1  = self.s_t1.normalize(self._g_noNones_t1)
		self._segments_t1 = _su.segmentateData(self._normalized_t1)
		##### NORMALIZE AND THEN SEGMENTATE T1
		_su = SessionUtils(self.s_t2)
		self._g_noNones_t2 =  _su.removeNones(self._grouped_t2)
		self._normalized_t2  = self.s_t2.normalize(self._g_noNones_t2)
		self._segments_t2 = _su.segmentateData(self._normalized_t2)

	def classify(self,save=False):
		#Labels [y]
		#0 = no   anxiety
		#1 = mild anxiety
		#2 = high anxiety
		X = np.array( [self._segments_sample[0],self._segments_t1[0],self._segments_t2[0]])
		y = [0,1,2]
		clf = svm.SVC(kernel='linear', C=1.0)
		y_pred = clf.fit(X, y)

		results = []
		r = []
		for _x, _segment in enumerate(self._segments_sample):
			r.append( int(clf.predict(_segment)))
		results.append(r)
		r = []
		for _x, _segment in enumerate(self._segments_t1):
			r.append( int(clf.predict(_segment)))

		results.append(r)
		r = []

		for _x, _segment in enumerate(self._segments_t2):
			r.append( int(clf.predict(_segment)))
		results.append(r)
		r = []

		######################SAVE TO DISK
		if(save):
			with open("results.txt","w") as _file:
				for r in results:
					for _v in r:
						_file.write(str(_v))
					_file.write("\n")
		print results
		return results

if __name__ == "__main__":
	m = Ml("data/n2/n2_sample/1425405680330/","data/n2/n2_1/1425406094608/","data/n2/n2_2/1425407232389/")
	m.classify()
