"""

"""
from random import random
# primelist = []
# upper = 100000
# lower = 19090
class PrimeNo(object):
    def __init__(self, lower = 5000 , upper = 10000, primelist = []):
        self.upper = upper
        self.lower = lower
        self.primelist = primelist

    def prime(self):
        for x in range( self.lower, self.upper):
            for y in range(2, x):
                if True:
                    if x % y == 0:
                        break
                    else:
                        self.primelist.append(x)



        return  list(set(self.primelist))


