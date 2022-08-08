#----------------------------CYTHON LIBRARIES----------------------------#
cimport numpy as np
cimport cython
from libc.math cimport sqrt, acos, pi, fabs, exp

#----------------------------PYTHON LIBRARIES----------------------------#
import numpy as np
import random

@cython.boundscheck(False) # turn off bounds-checking
@cython.wraparound(False)  # turn off negative index wrapping
@cython.cdivision(True)
cdef long moduloC(long a, long b):
    cdef long res =  a % b
    if  res >= 0: return res
    else: return res + b

@cython.boundscheck(False) # turn off bounds-checking
@cython.wraparound(False)  # turn off negative index wrapping
cdef list sampling_wo_replacement(int N, int max_int):
    
    cdef int i
    cdef list points = list(range(max_int))

    random.shuffle(points)

    return points[:N]

@cython.boundscheck(False) # turn off bounds-checking
@cython.wraparound(False)  # turn off negative index wrapping
cpdef list grid_setup(int N, double width, double L):

    cdef list grid = []
    cdef int i, j, k, n, l
    cdef int max_points_l = int(L // width)
    cdef int max_points = (max_points_l)**3
    cdef int pos
    cdef int x, y, z

    grid_points = sampling_wo_replacement(N = N, max_int = max_points)

    n = 0
    

    for i in range(N):

        x = (grid_points[i] // max_points_l) // max_points_l
        y = moduloC((grid_points[i] // max_points_l), max_points_l)
        z = moduloC(grid_points[i], max_points_l)

        grid.append([ float(x) * width + width / 2, float(y) * width + width / 2, float(z) * width + width / 2])


    return grid



