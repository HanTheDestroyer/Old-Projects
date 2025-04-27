import os
from numba import jit
import numpy as np


os.environ['NUMBA_CUDA_DEVICE'] = '0'


@jit(nopython=True)
def sandpile_simulation(sandpile):
    while True:
        new_grid = np.zeros_like(sandpile, dtype='int')

        for i in range(sandpile.shape[0]):
            for j in range(sandpile.shape[1]):
                if sandpile[i, j] < 4:
                    new_grid[i, j] = sandpile[i, j]

        row_ind, col_ind = np.where(sandpile >= 4)
        for c in range(len(row_ind)):
            i, j = row_ind[c], col_ind[c]
            new_grid[i, j] = sandpile[i, j] - 4
            if i < 639:
                new_grid[i + 1, j] += 1
            if i > 0:
                new_grid[i - 1, j] += 1
            if j < 639:
                new_grid[i, j + 1] += 1
            if j > 0:
                new_grid[i, j - 1] += 1

        sandpile = new_grid
        if len(row_ind) == 0:
            break

    return sandpile


grid = np.zeros([640, 640], dtype='int')
grid[320][320] = 5000


result = sandpile_simulation(grid)

np.savetxt('sandpile_result.txt', result, fmt='%d')
