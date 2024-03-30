

import sys 
import subprocess
import numpy as np
def assert_same_metrix(metrix1, metrix2):
    m1 = np.array(metrix1)
    m2 = np.array(metrix2)
    maxv = np.max(np.abs(m1 - m2))
    # print(m1)
    assert(maxv <= 0.00001)
here = False
def get_rank_from_file(filename):
    # Format < ((rowstart, rowend), (colstart, colend), (col2start, col2end)), 2x list of (row_id, url, initial Rank) list of [list of 0 and 1]]> , Note that the list is transpose already so it store the row that go into row_id

    metrix_dict = {}
    for line in open(filename).readlines():
        key, value =  line.strip().split('\t')
        matrix1 = eval(value)[0][1]
        matrix2 = eval(value)[1][1]
        key = eval(key)
        first  = (key[0][0] ,key[0][1])
        second = (key[1][0] ,key[1][1])
        third = (key[2][0] ,key[2][1])
        range1 = (first, second)
        range2 = (second, third)
        
        if metrix_dict.get(range1) == None:
            metrix_dict[range1] = matrix1
        if metrix_dict.get(range2) == None:
            metrix_dict[range2] = matrix2

        metrixstore = metrix_dict[range1]
        metrixstore2 = metrix_dict[range2]
        assert_same_metrix(metrixstore, matrix1)
        assert_same_metrix(matrix2, metrixstore2)
        
    a = ((0,49), (0,49))
    b = ((0,49), (49,99))
    c = ((49,99), (0,49))
    d = ((49,99), (49,99))
    full_matrix = np.zeros((99,99))
    full_matrix[0:49, 0:49] = metrix_dict[a]
    full_matrix[0:49, 49:99] = metrix_dict[b]
    full_matrix[49:99, 0:49] = metrix_dict[c]
    full_matrix[49:99, 49:99] = metrix_dict[d]
    full_matrix = np.array(full_matrix)
    print(full_matrix)
    if(here):
        return
    for i in range(10):
        print(i)
        full_matrix = full_matrix @ full_matrix
        print(full_matrix)
    print(np.sum(full_matrix,axis = 0))

intial_file_name = "../4.matrix_multiplication/multiply_0_input.txt"
get_rank_from_file(intial_file_name)
id = 2
here = True
while True:
    file = "../5.rank_calculation/rank_" + str(id) + "_reducer_output.txt"
    get_rank_from_file(file)
    id += 2
    if(id > 10):
        break