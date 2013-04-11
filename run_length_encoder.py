import numpy as NP

#generate a random int array
x = NP.random.randint(0,3,100)
print str(x)+' is encoded to'
run_starts, = NP.where(NP.diff(NP.hstack(([0], x, [0]))) != 0)
print [x[run_starts[i]] if (run_starts[i+1] == run_starts[i]+1) else (x[run_starts[i]], run_starts[i+1]-run_starts[i]) for i in range(len(run_starts)-1)]


