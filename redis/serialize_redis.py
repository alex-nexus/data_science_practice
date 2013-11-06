from time import time
import numpy as NP
from redis import StrictRedis as redis
A = 10 * NP.random.randn(10000).reshape(1000, 10)

# flatten the 2D NumPy array and save it as a binary string
array_dtype = A.dtype
l, w = A.shape
As = A.ravel().tostring()

# create a key as a UNIX timestamp w/ array shape appended to end of key delimited by '|'
db = redis(db=0)
key = '{0}|{1}#{2}|{3}'.format(int(time()), l, w, A.dtype)

# store the binary string in redis
db.set(key, As)
 
# retrieve the proto-array from redis
As = db.get(key)
 
# deserialize it 
l, w = key.split('|')[1].split('#')
atype = key.split('|')[2]

A2 = NP.fromstring(As, dtype=atype).reshape(int(l), int(w))
print A==A2
print A2
