# Input: <url, [outlink-url]>
# Output: <url, (rank, [outlink-url])>
# Mapper 

import sys
import json 

outlink_url_list = []

distributed_file_cache = open("../pagerank.txt").readlines() # rank and url
old_rank = {}
for line in distributed_file_cache:
    rank, url = line.strip().split('\t')
    old_rank[url] = rank

inputs = []
all_url = []
for line in sys.stdin: 
    url, value_str = line.strip().split('\t')
    outlink_url = eval(value_str)
    inputs.append( (url, outlink_url))
    all_url.append(url)
    all_url += outlink_url

all_url = set(all_url)
n = len(all_url)
old_url = all_url & set(old_rank.keys())
new_url = all_url - old_url

# print(len(old_url), len(new_url))
new_initial_rank = {}
total_rank = 0
for url in old_url:
    new_initial_rank[url] = old_rank[url] + 1.0 / n 
    total_rank += new_initial_rank[url]
for url in new_url:
    new_initial_rank[url] = 1.0 / n
    total_rank += 1.0 / n

# Normalize
for url, out_url in inputs:
    rank = new_initial_rank[url]
    value = (rank/total_rank , out_url)
    print(f"{url}\t{json.dumps(value)}")

