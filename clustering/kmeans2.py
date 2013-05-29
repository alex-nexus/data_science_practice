import numpy as NP
import matplotlib

matplotlib.use('Agg')
from scipy.cluster.vq import *
import pylab

#generate 100 data points with 3 attributes
NP.set_printoptions(precision=3, linewidth=100, suppress=True)

data_point = 1000
dim = 2
iter_max = 100
k = 3
threshold = 0.01

#generate data
data = 10 * NP.random.randn(data_point, 2)

#data = NP.random.randint(0, 100, data_point * dim).reshape(data_point, dim)
print 'data'
print data

#initialization:pick 3 random centroids
cs = NP.random.randint(0, data.shape[0], k)
cs = range(k)
cxs = NP.zeros((k, 2), dtype=NP.float)
cxs = data[cs, :]
print 'initial centroids'
print cxs

dm = NP.zeros((data_point, k), dtype=NP.float)
iter = 0
while iter < iter_max:
    old_cxs = NP.array(cxs, copy=True)
    iter += 1

    #compute distance matrix by broadcasting into an extra dimension
    dm = NP.sqrt(NP.sum((data.reshape(1, data_point, dim) - cxs.reshape(k, 1, dim)) ** 2, axis=2)).T

    #cluster each points to a centroid
    cls = NP.argmin(dm, axis=1)

    #compute the new centroids
    for i in range(k):
        cxs[i, :] = NP.mean(data[NP.where(cls == i), :], axis=1)[:, 0:2]

    print 'th: ' + str(NP.sum(NP.fabs(cxs - old_cxs)))
    if NP.sum(NP.fabs(cxs - old_cxs)) < threshold: break

print str(iter) + ' iterations'
print cxs

#graph
colors = ([([0.4, 1, 0.4], [1, 0.4, 0.4], [0.1, 0.8, 1])[i] for i in cls])

# plot colored points
pylab.scatter(data[:, 0], data[:, 1], c=colors)

# mark centroids as (X)
pylab.scatter(cxs[:, 0], cxs[:, 1], marker='o', s=500, linewidths=2, c='none')
pylab.scatter(cxs[:, 0], cxs[:, 1], marker='x', s=500, linewidths=2)

pylab.savefig('kmeans2.png')