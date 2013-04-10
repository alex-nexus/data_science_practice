import numpy as NP

x = NP.random.randint(0,3,10)
x = [1,1,2,2,2,3,1,1,1,0,0,1]
print x

run_starts, = NP.where(NP.diff(NP.hstack(([0], x, [0]))) != 0)

a = []
for i in range(len(run_starts)-1):
  #print i, run_starts[i], run_starts[i+1]
  pos = run_starts[i]
  print i, pos
  if (run_starts[i+1] == run_starts[i]+1): #no encode
    print 'b'
    element = x[pos]    
  else:
    print 'c'
    element = (x[pos], run_starts[i+1]-run_starts[i])
  print element 
  a.append(element)  
  
print a


