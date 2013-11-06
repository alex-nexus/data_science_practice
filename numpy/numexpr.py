import numpy as NP
import numexpr as NE
import timeit


a = NP.arange(1e6)
b = NP.arange(1e6)

print a.dtype

print NE.evaluate("a + 1")
print NE.evaluate('a*b-4.1*a > 2.5*b')

timeit.timeit('NE.evaluate("a**2 + b**2 + 2*a*b")')