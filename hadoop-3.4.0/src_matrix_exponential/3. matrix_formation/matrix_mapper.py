# Input : <url, (rank, [outlink-url])>
# Output : <row_id, [url, initial Rank, [list of 0 and 1]]>

import sys
import numpy as np
import json 

distributed_file_cache = open("../../src_iterative/2.graphformation/graph_2_reducer_output.txt").readlines() # rank and url
url2id = {}
id = 0
for line in distributed_file_cache:
    url, _ = line.strip().split('\t')
    url2id[url] = id 
    id += 1

n = len(url2id.keys())
ALPHA = 0.8
for line in sys.stdin:
    url, value = line.strip().split('\t')
    rank, outlink = eval(value)
    adj_matrix = [0 for i in range(n)]
    outlink = list(set(outlink))
    # print(len(outlink))
    
    for link in outlink:
        adj_matrix[ url2id[link] ] = 1.0 / len(outlink)
    if len(outlink) == 0: ## To not create Dead end but spider trap ok
        adj_matrix[ url2id[url] ] = 1
    # print(adj_matrix)
    # print(abs(np.array(adj_matrix).sum()))
    assert( abs(np.array(adj_matrix).sum() - 1) < 0.001)
    adj_matrix = [i * ALPHA + (1 - ALPHA)/n for i in adj_matrix]
    # print(abs(np.array(adj_matrix).sum() - 1))  
    assert( abs(np.array(adj_matrix).sum() - 1) < 0.001)
    newval = (url, rank, adj_matrix)
    #print(newval)
    print(f"{url2id[url]}\t{json.dumps(newval)}")