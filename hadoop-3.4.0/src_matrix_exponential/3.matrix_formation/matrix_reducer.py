# Input : <row_id, [url of row_id, initial Rank, [list of 0 and 1]]>
# Output : < ((rowstart, rowend), (colstart, colend)), list of (row_id, url, initial Rank) list of [list of 0 and 1]]> , Note that the list is transpose already so it store the row that go into row_id

import sys 
import numpy as np
import json 

# Print Change the following range manually 
# label row     col
#  a    (0,n/2)  (0,n/2)
#  b    (0,n/2)  (n/2,n) 
#  c    (n/2,n)     (0,n/2)
#  d    (n/2,n)     (n/2,n)

n = len(open("../../src_iterative/2.graphformation/graph_2_reducer_output.txt").readlines())
reducer_row_range = (0, n//2)
#reducer_row_range = (n//2, n)

reducer_col_range = (0, n//2)
reducer_col_range = (n//2, n)

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
        new_adj_matrix[row_id] = np.array(adj_matrix[reducer_row_range[0]: reducer_row_range[1]], dtype = float)

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