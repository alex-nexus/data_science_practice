import numpy as NP

#generate a random int array
x = NP.random.randint(0,3,10)
print str(x)+' is encoded to'
run_starts, = NP.where(NP.diff(NP.hstack(([-100], x, [-100]))) != 0)
encoded = [x[s] if (e==s) else (x[s], e-s+1) for s, e in zip(run_starts[:-1], NP.roll(run_starts-1, -1)[:-1])]
print encoded
