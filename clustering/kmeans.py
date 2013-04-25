import numpy as NP
import matplotlib
matplotlib.use('Agg')
from scipy.cluster.vq import *
import pylab

#generate 100 data points with 3 attributes

pylab.close()

# generate 3 sets of normally distributed points around
# different means with different variances
pt1 = NP.random.normal(1, 0.2, (100,2))
pt2 = NP.random.normal(2, 0.5, (300,2))
pt3 = NP.random.normal(3, 0.3, (100,2))

# slightly move sets 2 and 3 (for a prettier output)
pt2[:,0] += 1
pt3[:,0] -= 0.5

xy = NP.concatenate((pt1, pt2, pt3))

# kmeans for 3 clusters
res, idx = kmeans2(NP.array(zip(xy[:,0],xy[:,1])),3)

print res
print idx

colors = ([([0.4,1,0.4],[1,0.4,0.4],[0.1,0.8,1])[i] for i in idx])

# plot colored points
pylab.scatter(xy[:,0],xy[:,1], c=colors)

# mark centroids as (X)
pylab.scatter(res[:,0],res[:,1], marker='o', s = 500, linewidths=2, c='none')
pylab.scatter(res[:,0],res[:,1], marker='x', s = 500, linewidths=2)

pylab.savefig('kmeans.png')