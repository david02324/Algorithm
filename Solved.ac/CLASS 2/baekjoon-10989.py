import sys
a = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    a[int(sys.stdin.readline())] += 1

for i in range(len(a)):
    for j in range(a[i]):
        print(i)