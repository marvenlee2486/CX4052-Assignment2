import sys 
import subprocess

intial_file_name = "../2.graphformation/graph_2_reducer_output.txt"
def get_rank_from_file(filename):
    rank_dict = {}
    total_rank = 0
    for line in open(filename).readlines():
        url, struct =  line.strip().split('\t')
        rank = eval(struct)[0]
        rank_dict[url] = rank
        
        total_rank += rank
    print(total_rank)
    return rank_dict

def compare_two_file_rank(rank1_dict, rank2_dict):
    maxv = 0
    for url, rank1 in rank1_dict.items():
        rank2 = rank2_dict[url]
        maxv = max(maxv, abs(rank1 - rank2))
    return maxv
ERROR = 0.0000001

current_rank = get_rank_from_file(intial_file_name)
# rint(current_rank)
id = 1
input = intial_file_name
while True:
   
    output = "compute_" + str(id) + "_mapper_output.txt"
    command = f"python3 compute_mapper.py < {input} > {output}"
    subprocess.run([command],shell = True)

    next_input = "compute_" + str(id + 1) + "_reducer_output.txt"
    command = f"python3 compute_reduce.py < {output} > {next_input}"
    subprocess.run([command], shell = True)

    new_rank = get_rank_from_file(next_input)
    max_diff = compare_two_file_rank(new_rank, current_rank)
    if(max_diff < ERROR):
        print(max_diff)
        break
    id += 2
    current_rank = new_rank
    input = next_input

