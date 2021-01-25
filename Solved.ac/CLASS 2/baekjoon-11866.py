n,k = map(int,input().split())
arr = [i for i in range(1,n+1)]
li = []
idx = 0
while arr:
   idx = (idx + k - 1) % len(arr)
   li.append(str(arr.pop(idx)))

print('<'+', '.join(li)+'>')