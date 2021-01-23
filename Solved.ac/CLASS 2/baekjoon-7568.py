weight = []
height = []
n = int(input())
for _ in range(n):
    w,h = map(int,input().split())
    weight.append(w)
    height.append(h)

ranks = [1] * n
for i in range(n):
    for j in range(n):
        if weight[j] > weight[i] and height[j] > height[i]:
            ranks[i] += 1

for rank in ranks:
    print(rank)