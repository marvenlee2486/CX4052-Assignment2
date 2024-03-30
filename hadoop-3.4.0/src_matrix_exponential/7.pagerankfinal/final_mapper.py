# Output: < ((rowstart, rowend), (colstart, colend), (col2start, col2end)), 2x list of (row_id, url,  Rank) list of [list of 0 and 1]]> , Note that the list is transpose already so it store the row that go into row_id

import sys

for line in sys.stdin:
    _, struct = line.strip().split('\t')
    rank_tuple = eval(struct)[0][0]
    rank_tuple2 = eval(struct)[1][0]

    for tuple in rank_tuple:
        print(f"{tuple[2]}\t{tuple[1]}")
