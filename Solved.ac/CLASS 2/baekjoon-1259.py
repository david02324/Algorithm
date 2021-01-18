arr = []
while True:
    arr.append(input())
    if arr[-1] == '0':
        arr.pop()
        break

for obj in arr:
    if len(obj) == 1:
        print('yes')
    for i in range(len(obj) // 2):
        if obj[i] == obj[-1*(i+1)]:
            if i == len(obj) // 2 - 1:
                print('yes')
        else:
            print('no')
            break