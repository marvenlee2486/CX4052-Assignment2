
# Matrix [a b] [a b] = [a x a + b x c,  a x b + b x d] 
# Matrix [c d] [c d]   [c x a + d x c,  c x b + d x d]
# This is to distribute task to map for multiplication

import json
a = "../3. matrix_formation/matrix_2_a_reducer_output.txt"
b = "../3. matrix_formation/matrix_2_b_reducer_output.txt"
c = "../3. matrix_formation/matrix_2_c_reducer_output.txt"
d = "../3. matrix_formation/matrix_2_d_reducer_output.txt"

def convert(row, col):
    if(row == 0 and col == 0):
        return a 
    if(row == 0 and col == 1):
        return b 
    if(row == 1 and col == 0):
        return c
    if(row == 1 and col == 1):
        return d 

for first in range(0, 2):
    for second in range(0, 2):
        for third in range(0 ,2):
            m1 = convert(first, second)
            m2 = convert(second, third)

            key, value = open(m1).readlines()[0].strip().split('\t')
            key2, value2 = open(m2).readlines()[0].strip().split('\t')
            key = eval(key)
            value = eval(value)
            key2 = eval(key2)
            value2 = eval(value2)

            final_key = (key[0], key[1], key2[1])
            new_value = (value, value2)
            print(f"{json.dumps(final_key)}\t{json.dumps(new_value)}")
            

# command = f"python3 compute_mapper.py < {input} > {output}"
#    subprocess.run([command],shell = True)