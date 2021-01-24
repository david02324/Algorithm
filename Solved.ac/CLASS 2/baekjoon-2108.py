import sys
input = sys.stdin.readline

# 입력
data = []
for _ in range(int(input())):
    data.append(int(input()))
data.sort()

# 평균
avg = round(sum(data) / len(data))

# 중앙값
mid = data[len(data) // 2]

# 최빈값
counts = [0] * 8001
for number in data:
    counts[number+4000] += 1

mod = counts.index(max(counts)) - 4000
if counts.count(max(counts)) > 1:
    mod = counts.index(max(counts),mod + 4000 + 1) - 4000

# 범위
rng = max(data) - min(data)

# 출력
print(avg,mid,mod,rng,sep='\n')