import sys
input = sys.stdin.readline

k,n = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

left = 1
right = max(lans)

while left <= right:
    mid = (left + right) // 2
    count = 0
    for lan in lans:
        count += lan // mid
    
    if count >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)