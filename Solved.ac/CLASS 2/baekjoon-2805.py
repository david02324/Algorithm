# 시간 초과
# n, m = map(int,input().split())
# heights = list(map(int,input().split()))

# tempHeight = max(heights)
# while True:
#     myTree = 0
#     for tree in heights:
#         if tree - tempHeight > 0:
#             myTree += tree - tempHeight
    
#     if myTree >= m:
#         print(tempHeight)
#         break
#     else:
#         tempHeight -= 1

# 이진 탐색(Counter 이용)
from collections import Counter
n, m = map(int,input().split())
heights = Counter(map(int,input().split()))

left = 0
right = max(heights)

while left <= right:
    mid = (left + right) // 2
    myTree = 0
    for tree,count in heights.items():
        if tree > mid:
            myTree += (tree - mid) * count
    
    if myTree >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)