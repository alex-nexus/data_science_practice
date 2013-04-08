import numpy as np

class MatrixProcessor:

    def __init__(self):
        self.num_row = 100
        self.num_column = 100

        self.fname = "sample_data.csv"
        
        #sample_data = self.generate_sample_data()
        #self.write_data_to_csv(sample_data)
         
    def generate_sample_data(self):
        #write 1 line header
        self.headers = ','.join(['c'+str(x) for x in range(self.num_column)])
             
        #sample_data = np.random.randn(self.num_row, self.num_column)
        sample_data = np.random.randint(0, 100, self.num_row * self.num_column).reshape(self.num_row, self.num_column)
        return sample_data
        
    def write_data_to_csv(self, sample_data):
        csvfile = open(self.fname, 'wb')
        
        csvfile.write(self.headers)        

        #write to body as csv
        np.savetxt(csvfile, sample_data, delimiter=',', fmt='%d')
        
    def load_data_from_csv(self):
        #http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
        self.load_data = np.loadtxt(self.fname, delimiter=',', skiprows=1, dtype='int')
        print self.load_data       
       
    #mean centering for each feature
    def base_mean(self):
        print 'overall mean:' + str(np.mean(self.load_data))
        mean_per_column = np.mean(self.load_data, axis=0)
        print mean_per_column
        self.load_data
       
    def normalize_std(self):
        print 'normalize_std'
    



x = MatrixProcessor()
x.load_data_from_csv()
x.base_mean()
x.normalize_std()