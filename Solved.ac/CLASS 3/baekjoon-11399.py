_,li = input(),sorted(list(map(int,input().split())))
t = 0
total = 0
for p in li:
    t += p
    total += t

print(total)