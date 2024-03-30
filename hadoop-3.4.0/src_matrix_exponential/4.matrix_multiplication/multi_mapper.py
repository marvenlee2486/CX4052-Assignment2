# Input : < ((rowstart, rowend), (colstart, colend), (col2start, col2end)), 2x list of (row_id, url, initial Rank) list of [list of 0 and 1]]> , Note that the list is transpose already so it store the row that go into row_id
# Output: < ((rowstart, rowend), (colstart, colend)), list of (row_id, url, initial Rank) list of [list of 0 and 1]]
import sys 
import numpy as np
import json 

# Matrix [a b] [a b] = [a x a + b x c,  a x b + b x d] 
# Matrix [c d] [c d]   [c x a + d x c,  c x b + d x d]

for line in sys.stdin:
    responsible, value = line.strip().split('\t')
    row_range, col_range, col2_range = eval(responsible)
    matrix_1_resp = (row_range, col_range)
    matrix_2_resp = (col_range, col2_range)

    matrix_1, matrix_2 = eval(value)
    rank, matrix_1 = matrix_1 
    _, matrix_2 = matrix_2

    new_matrix = np.matmul(np.array(matrix_1),np.array(matrix_2))
    new_matrix = [[float(element) for element in row] for row in new_matrix]

    new_key = (row_range, col2_range)
    new_value = (rank, new_matrix)

    print(f"{json.dumps(new_key)}\t{json.dumps(new_value)}")

