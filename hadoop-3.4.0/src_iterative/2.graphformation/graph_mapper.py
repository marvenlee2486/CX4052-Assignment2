# Input: <url, [outlink-url]>
# Output: <url, [outlink-url]>
# Mapper 

import sys
import json 

outlink_url_list = []

distributed_file_cache = open("../1.crawler/crawler_4_reduce_output.txt").readlines()
distributed_file_cache = [line.strip().split('\t')[0] for line in distributed_file_cache]

for line in sys.stdin: 
    url, value_str = line.strip().split('\t')
    outlink_url = eval(value_str)
    outlink_url = [link for link in outlink_url if link in distributed_file_cache]
    outlink_url = list(set(outlink_url))
    print(f"{url}\t{json.dumps(outlink_url)}")


