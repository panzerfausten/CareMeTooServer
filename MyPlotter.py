import pylab as plt
import numpy as np

class MyPlotter:
        def __init__(self,title,data,labelX,labelY,limy=None):
                self.data = data
                self.title = title
		self.labelX = labelX
		self.labelY = labelY
		self.limy = limy
		print self.limy

        def plot(self,outputFigure):
                #init the plot
                fig, ax = plt.subplots()
                index = np.arange(len (self.data))
                bar_width = 1
                ax.plot(self.data,color='red')
                #ax.set_ylabel("%s value" %(self.e3data.dataType))
                ax.set_xlabel(self.labelX)
                ax.set_ylabel(self.labelY)
                ax.set_title(self.title)
		plt.ylim(self.limy)
                plt.grid(True)
                plt.savefig(outputFigure)
		

