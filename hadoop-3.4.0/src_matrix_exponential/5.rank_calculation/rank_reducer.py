# Input: < ((rowstart, rowend), (colstart, colend)), list of (row_id, url, temp new Rank) list of [list of 0 and 1]]
# Output: < ((rowstart, rowend), (colstart, colend), (col2start, col2end)), 2x list of (row_id, url, initial Rank) list of [list of 0 and 1]]> , Note that the list is transpose already so it store the row that go into row_id
# (0,0) (0,1) x 0 =  (0,0)(0) + (0,1)(1)
# (1,0) (1,1)   1    (1,0)(0) + (1,1)(1)

import sys 
import json 
import numpy as np

rank_range = {}
matrix_range = {}

for line in sys.stdin:
    key, value = line.strip().split('\t')
    temp_rank, orimatrix = eval(value)
    # print(temp_rank)
    row_range, col_range = eval(key)
    row_range = (row_range[0], row_range[1])
    col_range = (col_range[0], col_range[1])
    
    if rank_range.get(row_range) == None:
        rank_range[row_range] = []

    rank_range[row_range].append(temp_rank)
    # print(key)
    # print(orimatrix)
    matrix_range[(row_range, col_range)] = orimatrix

# Calculate New rank
new_rank_range ={}  
for row_range, value in rank_range.items():
    rank1 = value[0]
    rank2 = value[1]
    newrank = []
    if(rank1[0][0] != -1):
        for i in range(len(rank1)):
            newrank.append((rank1[i][0], rank1[i][1], rank1[i][2] + rank2[i][2]))
    else:
        for i in range(len(rank2)):
            newrank.append((rank2[i][0], rank2[i][1], rank1[i][2] + rank2[i][2]))
    new_rank_range[row_range] = newrank

# Assertion for testing
# for rang, new_rank in new_rank_range.items():
#     print(rang, new_rank)

for range1, matrix1 in matrix_range.items():
    for range2, matrix2 in matrix_range.items():
        if range1[1] != range2[0]:
            continue
        new_range = (range1[0], range1[1], range2[1])
        new_value = ((new_rank_range[(range1[0][0], range1[0][1])], matrix1),(new_rank_range[(range2[0][0], range2[0][1])], matrix2))
        print(f"{json.dumps(new_range)}\t{json.dumps(new_value)}")
# print(new_rank_range)
