# 덱(deque)을 사용한 풀이
from collections import deque

n = int(input())
cards = deque([i for i in range(1,n+1)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())

# 규칙성을 찾는 풀이
n,t=int(input()),1
# 1이 입력일 경우 거름
if n == 1:
  print(1)
  exit()
  
while True:
    t *= 2
    if t >= n:
      t //= 2
      break
print((n-t)*2)
