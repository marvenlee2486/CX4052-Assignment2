# Input : <row_id, [url of row_id, initial Rank, [list of 0 and 1]]>
# Output : < ((rowstart, rowend), (colstart, colend)), list of (row_id, url, initial Rank) list of [list of 0 and 1]]> , Note that the list is transpose already so it store the row that go into row_id

import sys 
import numpy as np
import json 

reducer_row_range = (0, 49)
# reducer_row_range = (49, 99)

reducer_col_range = (0, 49)
# reducer_col_range = (49, 99)

row_id2url = {}
new_adj_matrix = {}
# Sort of read and shuffle phase
for line in sys.stdin:
    row_id, value = line.strip().split('\t')
    row_id = int(row_id)
    url, rank, adj_matrix = eval(value)
    if(row_id >= reducer_row_range[0] and row_id < reducer_row_range[1]):
        row_id2url[row_id] = (row_id, url, rank)
    if(row_id >= reducer_col_range[0] and row_id < reducer_col_range[1]):   
        new_adj_matrix[row_id] = np.array(adj_matrix[reducer_row_range[0]: 99], dtype = float)

n = len(list(new_adj_matrix.keys()))

# Reduce by transposing the matrix 
matrix = []
for row_id in range(reducer_col_range[0], reducer_col_range[1]):
    matrix.append(new_adj_matrix[row_id])

matrix = np.array(matrix)
# print(matrix.shape)
# print(np.sum(matrix, axis = 1))
matrix = matrix.transpose()
# print(matrix.shape)
# print(np.sum(matrix, axis = 0))
matrix = [[float(element) for element in row] for row in matrix ]

rank_vector = []
for row_id in range(reducer_row_range[0], reducer_row_range[1]):
    rank_vector.append(row_id2url[row_id])

key = (reducer_row_range, reducer_col_range)
value = (rank_vector, matrix)
print(f"{json.dumps(key)}\t{json.dumps(value)}")