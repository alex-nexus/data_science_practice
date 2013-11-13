import numpy as NP
f = open('order_ts.csv', 'r')


nts = NP.zeros(2500000, dtype=NP.int)
i=0
for line_string in f.readlines():
    timestamp = line_string.strip().split(',')[0]
    nts[i] = timestamp
    i+=1
            
            
nts_diff = NP.diff(nts)                    
f.close()