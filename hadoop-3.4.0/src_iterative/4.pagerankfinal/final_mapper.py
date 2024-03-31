# Input: <url, (Rank,  [list of outlink-url of url])
# Output: <Rank, url>)

import sys

for line in sys.stdin:
    url, struct = line.strip().split('\t')
    rank = eval(struct)[0]
    print(f"{rank}\t{url}")