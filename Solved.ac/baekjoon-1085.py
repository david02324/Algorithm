arr = input().split()
x = int(arr[0])
y = int(arr[1])
w = int(arr[2])
h = int(arr[3])

distance = min(w-x,h-y,x,y)

print(distance)