# Input: <outlink-url, (url, initialRank of url,  [list of outlink-url of url])>
# Output: <url, (Rank,  [list of outlink-url of url])

import sys
import json 
ALPHA = 0.8
inputs = {}
all_url = []
for line in sys.stdin:
    outlink_url, value = line.strip().split('\t')
    if inputs.get(outlink_url) == None:
        inputs[outlink_url] = []
    unpack = eval(value)
    all_url.append(outlink_url)
    all_url.append(unpack[0])

    inputs[outlink_url].append(unpack)

all_url = list(set(all_url))
n = len(all_url)
#  print(n)

new_rank_dict = {}
url_outlink = {}
for out_url, struct_list in inputs.items():
    new_rank = 0
    processed_url = []
    for struct in struct_list:
        # if struct[0] in processed_url: ## TO ensure no duplication
        #     continue
        if url_outlink.get(struct[0]) == None:
            url_outlink[struct[0]] = struct[2]

        processed_url.append(struct[0])
        new_rank += struct[1] / len(struct[2])
    
    new_rank = ALPHA * new_rank + (1 - ALPHA) / n
    new_rank_dict[out_url] = new_rank

for no_in_url in set(all_url) - set(inputs.keys()):
    new_rank_dict[no_in_url] = (1 - ALPHA) / n

# total = 0
for url, rank in new_rank_dict.items():
    list_out = []
    # total += rank
    if url_outlink.get(url) != None:
        list_out = url_outlink[url]
    value = (rank, list_out  )
    print(f"{url}\t{json.dumps(value)}")

# print(total, 1)