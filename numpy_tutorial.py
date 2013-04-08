import numpy as np

num_row = 100000
num_column = 100

fname = "sample_data.csv"

#headers = ','.join(['c'+str(x) for x in range(num_column)]) 

#generate sample data 
#sample_data = np.random.randn(num_row, num_column)
#sample_data = np.random.randint(0, 100, num_row * num_column).reshape(num_row, num_column)

#write to csv
#csvfile = open(fname, 'wb')

#write 1 line header
#csvfile.write(headers)

#write to body as csv
#np.savetxt('sample_data.csv', sample_data, delimiter=',', fmt='%d')


##########

#http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
load_data = np.loadtxt(fname, delimiter=',', skiprows=1, dtype='int')
print load_data



print 'mean:' + str(np.mean(load_data))
mean_per_column = np.mean(load_data, axis=0)

print mean_per_column

#mean centering for each feature


#std = 1
