import numpy as NP
import math
#generate 100 data points with 3 attributes
data = NP.random.randint(0, 100, 300).reshape(100, 3)
print 'data'
print data

k=3
#initialization:pick 3 random centroids
cs = NP.random.randint(0, data.shape[0], k)
cxs = data[cs,:]

dm = NP.zeros(data.shape)
iter = 0
while iter < 100:
    old_cxs = NP.array(cxs, copy=True)
    iter+=1
    
    #compute distance matrix
    for i, cx in enumerate(cxs):
        dm[:,i] = NP.sqrt(NP.sum((data-cx)**2, axis=1))
        
    #assign each points to a centroid
    cls = NP.argmin(dm, axis=1)
    
    #compute the new centroids
    for i in range(k):
        cxs[i, :] = NP.mean(dm[NP.where( cls == i), :], axis=1)
    
    if NP.sum(NP.fabs(cxs - old_cxs)) < 4: break 

print iter
print cxs