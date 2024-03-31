

import sys 
import subprocess


def get_rank_from_file(filename):
    # Format < ((rowstart, rowend), (colstart, colend), (col2start, col2end)), 2x list of (row_id, url, initial Rank) list of [list of 0 and 1]]> , Note that the list is transpose already so it store the row that go into row_id

    rank_dict = {}
    for line in open(filename).readlines():
        _, value =  line.strip().split('\t')
        rank1 = eval(value)[0][0]
        rank2 = eval(value)[1][0]
        rank_iterate = rank1 + rank2 
        # print(len(rank1), len(rank2), len(rank_iterate))

        for rank_tuple in rank_iterate:
            row_id = rank_tuple[0]
            url = rank_tuple[1]
            rank = rank_tuple[2]
            
            if rank_dict.get(row_id) == None:
                rank_dict[row_id] = (url, rank)
    total_rank = 0
    for row_id, struct in rank_dict.items():
        total_rank += struct[1]
    print(total_rank)
    return rank_dict

def compare_two_file_rank(rank1_dict, rank2_dict):
    maxv = 0
    for row_id, struct in rank1_dict.items():
        _, rank1 = struct
        rank2 = rank2_dict[row_id][1]
        maxv = max(maxv, abs(rank1 - rank2))
    return maxv
ERROR = 0.0000001
intial_file_name = "../4.matrix_multiplication/multiply_0_input.txt"
current_rank = get_rank_from_file(intial_file_name)

id = 1
input = intial_file_name
while True:
    print(id //2, "iteration")
    output = "../4.matrix_multiplication/multiply_" + str(id) + "_mapper_output.txt"
    command = f"python3 ../4.matrix_multiplication/multi_mapper.py < {input} > {output}"
    subprocess.run([command],shell = True)

    next_input = "../4.matrix_multiplication/multiply_"  + str(id + 1) + "_reducer_output.txt"
    command = f"python3 ../4.matrix_multiplication/multi_reducer.py < {output} > {next_input}"
    subprocess.run([command], shell = True)

    input = next_input
    output = "../5.rank_calculation/rank_" + str(id) + "_mapper_output.txt"
    command = f"python3 ../5.rank_calculation/rank_mapper.py < {input} > {output}"
    subprocess.run([command],shell = True) 

    next_input = "../5.rank_calculation/rank_"  + str(id + 1) + "_reducer_output.txt"
    command = f"python3 ../5.rank_calculation/rank_reducer.py < {output} > {next_input}"
    subprocess.run([command], shell = True)

    new_rank = get_rank_from_file(next_input)
    max_diff = compare_two_file_rank(new_rank, current_rank)
    # print(new_rank)
    # print(max_diff)
    if(max_diff < ERROR):
        # print(max_diff)
        break
    id += 2
    current_rank = new_rank
    input = next_input

