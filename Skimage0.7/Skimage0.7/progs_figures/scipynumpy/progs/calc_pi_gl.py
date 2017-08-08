#!/usr/bin/python

import time

#  This script calculates Pi by 
#  iterating the Gregory-Leibniz series.
#  Nicholas Labello
#  Minnesota Supercomputing Institute

t1 = time.clock()

numer = 4.0  # Inline comments are okay
denom = 1.0
sum = 0
counter = 0
numIter = 10000000


while counter < numIter: 
    sum   = sum + numer/denom
    denom = denom + 2
    sum   = sum - numer/denom
    denom = denom + 2
    counter = counter + 1

print sum

t2 = time.clock()
timetaken = t2-t1;
print "Time taken = %f seconds" % timetaken