from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = numpy.ones((3,3))
    data[1,1] = 3.0	
else:
    pass
data = comm.bcast(data, root=0)
print "rank = ",rank
print "data = ",data