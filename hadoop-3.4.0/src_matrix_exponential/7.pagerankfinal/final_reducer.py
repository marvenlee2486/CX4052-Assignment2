#sorting

import sys

rank_dict = {}
for line in sys.stdin:
    rank, url = line.strip().split('\t')

    if(rank_dict.get(rank) == None):
        rank_dict[rank] = []
    rank_dict[rank].append(url)

sorted_dict = dict(sorted(rank_dict.items(), reverse = True))
for rank, v in sorted_dict.items():
    v = list(set(v))
    for url in v:
        print(f"{rank}\t{url}")