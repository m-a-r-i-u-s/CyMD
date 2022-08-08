#----------------------------CYTHON LIBRARIES----------------------------#
cimport numpy as np
cimport cython
from libc.math cimport sqrt, acos, pi, fabs, exp

#----------------------------PYTHON LIBRARIES----------------------------#
import numpy as np
import random

@cython.boundscheck(False) # turn off bounds-checking
@cython.wraparound(False)  # turn off negative index wrapping
cdef list norm_sample(int N, int max_int):
    
    cdef int i
    cdef list points = list(range(max_int))

    random.shuffle(points)

    return points[:N]
