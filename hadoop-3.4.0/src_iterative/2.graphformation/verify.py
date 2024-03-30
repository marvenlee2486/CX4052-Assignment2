import sys
total = 0
for line in sys.stdin:
    _ , score = line.split('\t')
    total += eval(score)
print(total)