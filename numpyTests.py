from numpy import *
random.rand(4,4)
randMat = mat(random.rand(4,4))
invRandMat = randMat.I
myEye = randMat*invRandMat
print(myEye)
print(myEye - eye(4))
