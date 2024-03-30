# Input: < ((rowstart, rowend), (colstart, colend)), list of (row_id, url, initial Rank) list of [list of 0 and 1]]
# Output: < ((rowstart, rowend), (colstart, colend)), list of (row_id, url, temp new Rank) list of [list of 0 and 1]]
# (0,0) (0,1) x 0 =  (0,0)(0) + (0,1)(0)
# (1,0) (1,1)   1    (1,0)(1) + (1,1)(1)

import sys 
import json 
import numpy as np

for line in sys.stdin:
    key, value = line.strip().split('\t')
    rank, orimatrix = eval(value)
    
    ## Asssertion
    rang = eval(key)
    for rank_tuple in rank:
        #print(rank_tuple[0], rang[1][0], rang[1][1])
        assert( (rank_tuple[0] >= rang[1][0]) and (rank_tuple[0] < rang[1][1]))

    matrix = np.array(orimatrix)
    rank_col_vector = [tup[2] for tup in rank]
    # print(len(rank_col_vector))
    # print(rang)
    # print(matrix.shape)
    # print(len(rank_col_vector))
    # print(rank)
    new_rank = matrix @ np.array(rank_col_vector)
    
    new_rank_struct = []
    i = 0
    # print(len(rank))
    range1, range2 = eval(key)
    if(range1 == range2):
        for tup in rank:
            # print(i, tup[0])
            tup[2] = float(new_rank[i])
            new_rank_struct.append(tup)
            i += 1
    else:
        new_rank_struct = [(-1, -1, number) for number in new_rank]
    #print(new_rank_struct)
    print(f"{key}\t{json.dumps((new_rank_struct, orimatrix))}")
