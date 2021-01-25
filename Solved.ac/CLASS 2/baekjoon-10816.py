# 이진 탐색
from bisect import bisect_left,bisect_right

N,numbers,M,targets = input(),list(map(int,input().split())),input(),list(map(int,input().split()))
numbers.sort()
counts = []

for target in targets:
    lidx = bisect_left(numbers,target)
    ridx = bisect_right(numbers,target)
    count = ridx - lidx
    counts.append(str(count))

print(' '.join(counts))

# Collections.Counter 이용
from collections import Counter
N,counts,M = input(),Counter(input().split()),input()
targets = input().split()
for target in targets:
    print(counts[target],end=' ')