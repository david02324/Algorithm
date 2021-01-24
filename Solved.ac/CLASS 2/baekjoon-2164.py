# 덱(deque)을 사용한 풀이
from collections import deque

n = int(input())
cards = deque([i for i in range(1,n+1)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())

# 2의 거듭제곱을 찾는 풀이
n,t=int(input()),1
while t < n:
    t *= 2
print(n*2 - t)