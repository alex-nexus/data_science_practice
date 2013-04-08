import numpy as np
import matplotlib.pyplot as plt

class MatrixProcessor:

    def __init__(self):
        self.num_row = 10
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
        
    #Reading in a CSV file    
    def load_data_from_csv(self):
        #http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
        self.load_data = np.loadtxt(self.fname, delimiter=',', skiprows=1, dtype='int')
    
    #Initial Processing
    def initial_processing(self):
       x.calculate_statistics()
       x.center_mean()
       x.normalize_std()
       #x.play() 
            
    def calculate_statistics(self):
        self.overall_mean = np.mean(self.load_data)
        
        self.mean_per_column = np.mean(self.load_data, axis=0)
        print 'mean_per_column:'+str(self.mean_per_column)
                    
        self.median_per_column = np.median(self.load_data, axis=0)
        #print 'median_per_column:'+str(self.median_per_column)
        
        self.std_per_column = np.std(self.load_data, axis=0)
        #print 'std_per_column:'+str(self.std_per_column)
        
        self.var_per_column = np.var(self.load_data, axis=0)
        #print 'var_per_column:'+str(self.var_per_column)
            
        self.cov = np.cov(self.load_data.T)
        print 'covariance matrix size:'+str(len(self.cov))+' '+str(self.cov)+''
        #print np.amin(self.load_data, axis=0)
        #print np.amax(self.load_data, axis=0)
    
    #mean centering for each feature
    def center_mean(self):   
        print 'center_mean'         
        self.load_data = self.load_data - self.mean_per_column
        
        #print self.load_data
                
    def normalize_std(self):
        print 'normalize_std'
        self.load_data = self.load_data / self.std_per_column
        
        self.std_per_column = np.std(self.load_data, axis=0)
        print 'new std_per_column:'+str(self.std_per_column)
    
        
    #Some Basic Description Statistics
    def 
        
x = MatrixProcessor()
x.load_data_from_csv()
x.initial_processing()