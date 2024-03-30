# Input : < ((rowstart, rowend), (colstart, colend)), list of (row_id, url, initial Rank) list of [list of 0 and 1]]
# Output: < ((rowstart, rowend), (col2start, col2end)), list of (row_id, url, initial Rank) list of [list of 0 and 1]]

import sys 
import numpy as np
import json 

# Matrix [a b] [a b] = [a x a + b x c,  a x b + b x d] 
# Matrix [c d] [c d]   [c x a + d x c,  c x b + d x d]

rank_range = {}
matrix_range = {}

for line in sys.stdin:
    responsible, value = line.strip().split('\t')
    row_range, col_range = eval(responsible)
    row_range = (row_range[0], row_range[1])
    col_range = (col_range[0], col_range[1])

    rank, matrix = eval(value)
    
    # To reduce the rank column vector
    if rank_range.get(row_range) == None:
        rank_range[row_range] = rank 
    
    # for reduce the matrix multiplication
    if matrix_range.get((row_range, col_range)) == None:
        matrix_range[(row_range, col_range)] = []
    matrix_range[(row_range, col_range)].append(matrix)

# test = np.zeros((99,99))
for key in matrix_range.keys():
    list_of_matrix = matrix_range[key]
    matrix1 = np.array(list_of_matrix[0])
    matrix2 = np.array(list_of_matrix[1])

    reduce_matrix = matrix1 + matrix2 
    reduce_matrix = [[float(ele) for ele in row] for row in reduce_matrix]
    rank = rank_range[key[1]]
    
    row, col = key 
    # test[row[0]:row[1],col[0]:col[1]] = reduce_matrix
    print(f"{json.dumps(key)}\t{json.dumps((rank, reduce_matrix))}")
# print(test)
# print(np.sum(test, axis = 0))