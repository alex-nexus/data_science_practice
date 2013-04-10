import numpy as NP

x = NP.random.randint(0,3,10)
x = [1,1,2,2,2,3,1,1,1,0,0,1]
run_starts, = NP.where(NP.diff(NP.hstack(([0], x, [0]))) != 0)

a = []
for i in range(len(run_starts)-1):
  #print i, run_starts[i], run_starts[i+1]
  pos = run_starts[i]
  if (run_starts[i+1] == run_starts[i]+1): #no encode
    element = x[pos]    
  else:
    element = (x[pos], run_starts[i+1]-run_starts[i])
  a.append(element)  
  
print x
print '->'
print a


