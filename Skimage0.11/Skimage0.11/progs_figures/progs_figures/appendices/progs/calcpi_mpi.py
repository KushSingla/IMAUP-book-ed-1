from mpi4py import MPI
import sys
import numpy as np
import time

def calc_partial_pi(rank,noofterms):
    start = rank*noofterms*2+1
    lastterm = start+(noofterms-1)*2
    denominator  = np.linspace(start,lastterm,noofterms)
    numerator = np.ones(noofterms)
    for i in range(0,noofterms):
        numerator[i] =  pow(-1,i+noofterms*rank)
        
    # Find the ratio and sum all the fractions 
    # to obtain pi value
    partialval =  sum(numerator/denominator)*4.0
    return partialval    
    
if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = MPI.COMM_WORLD.Get_size()
    totalnoterms = 1000000
    noofterms = totalnoterms/size
    
    partialval = calc_partial_pi(rank,noofterms)
    comm.Barrier()
    finalval = comm.reduce(partialval,op=MPI.SUM, root=0)
    if rank==0:
        print "The final value of pi is ",finalval
