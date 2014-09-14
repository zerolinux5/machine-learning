import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import array

group,labels = kNN.createDataSet()

print (group)
print (labels)

print kNN.classify0([0,0], group, labels, 3)

datingDataMat,datingLabels = kNN.fileToMatrix('datingTestSet2.txt')

print datingDataMat
print datingLabels[0:20]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2],15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()

normMat, ranges, minVals = kNN.autoNorm(datingDataMat)

print normMat
print ranges
print minVals