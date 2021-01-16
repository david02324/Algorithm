n = int(input())
answer = 0
for i in range(n):

    h = sum([int(i) for i in str(i)]) + i

    if(h==n):
        answer = i
        break

print(answer)