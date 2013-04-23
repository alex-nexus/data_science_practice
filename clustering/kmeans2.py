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
print 'centroids'
print cxs

dm = NP.zeros(data.shape)
iter = 0
while iter < 100:
    old_cxs = NP.array(cxs, copy=True)
    iter+=1
    print iter
    
    #compute distance matrix
    for i, cx in enumerate(cxs):
        dm[:,i] = NP.sqrt(NP.sum((data-cx)**2, axis=1))
        
    #assign each points to a centroid
    cls = NP.argmin(dm, axis=1)
    #dm = NP.column_stack((dm, NP.argmin(dm, axis=1)))
    print 'cls'
    print cls
    
    #compute the new centroids
    for i in range(k):
        cxs[i, :] = NP.mean(dm[NP.where( cls == i), :], axis=1)
    
    print 'new cxs'
    print cxs
        
    #print math.fabs(NP.sum(cxs - old_cxs))
    print NP.fabs(cxs - old_cxs)
    if NP.sum(NP.fabs(cxs - old_cxs)) < 4:
        break 

