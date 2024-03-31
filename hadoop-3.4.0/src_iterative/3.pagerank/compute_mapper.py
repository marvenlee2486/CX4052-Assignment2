# input : <url, (rank of url, [outgoing_url from url])
# output : <outlink-url, (url, initialRank of url, [list of outlink-url of url])>

import sys
import json 
for line in sys.stdin:
    url, value = line.strip().split("\t")
    rank, outgoing_link = eval(value)
    
    for outgoing_url in outgoing_link:
        print(f"{outgoing_url}\t{(url, rank, outgoing_link)}")
    if len(outgoing_link) == 0: # Convert dead end to spider trap
        print(f"{url}\t{json.dumps((url, rank, [url]))}")
