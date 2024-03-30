# input : <url, (rank of url, [outgoing_url from url])
# output : <outlink-url, (url, initialRank of url, [list of outlink-url of url])>

import sys
import json 
# all_url = []
for line in sys.stdin:
    url, value = line.strip().split("\t")
    rank, outgoing_link = eval(value)
    
    for outgoing_url in outgoing_link:
        # all_url.append(outgoing_url)
        # all_url.append(url)
        print(f"{outgoing_url}\t{(url, rank, outgoing_link)}")
    if len(outgoing_link) == 0: # Convert dead end to spider trap
        print(f"{url}\t{(url, rank, [url])}")
# all_url = list(set(all_url))
# print(len(all_url))