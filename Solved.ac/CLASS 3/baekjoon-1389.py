# dawitblog.tistory.com
from sys import stdin

n, m = map(int,input().split())

# 사람들 연결관계를 저장하는 리스트
people = [set() for _ in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    people[i].add(j)
    people[j].add(i)

l = [0] * (n+1)
print(people)
def find(steps,p,step):
    for person in people[p]:
        if not steps[person]:
            steps[person] = step
            find(steps,person,step+1)
            break

for i in range(1,n+1):
    steps = [0] * (n+1)
    steps[i] = 1
    find(steps,i,1)
    l[i] = sum(steps) - 1

print(l)