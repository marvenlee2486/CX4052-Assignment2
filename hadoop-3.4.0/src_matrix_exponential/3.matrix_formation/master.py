

lines = open("../../src_iterative/2.graphformation/graph_2_reducer_output.txt").readlines()

f1 = open("matrix_0_a_input.txt", 'w+')
f2 = open("matrix_0_b_input.txt", 'w+')

f1.write(''.join(lines[0:len(lines)//2]))
f2.write(''.join(lines[len(lines)//2 : len(lines)]))

