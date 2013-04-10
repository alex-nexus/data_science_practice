import numpy as NP

x = NP.random.randint(0,3,10)
x = [1,2,2,2,1,1,1,0,0,1]
diffs = NP.diff(NP.hstack(([0], x, [0])))
print x
print diffs

run_starts, = NP.where(diffs != 0)
#run_ends, = NP.where(diffs == 0)

print 'run starts'
print run_starts 

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


