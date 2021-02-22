l=list(map(int,input().split()))
if l[0] == 1:
    for i in range(1,8):
        if l[i] != i+1:
            print('mixed')
            break
        if i == 7:
            print('ascending')
elif l[0] == 8:
    for i in range(7,0,-1):
        if l[i] != 8-i:
            print('mixed')
            break
        if i == 1:
            print('descending')
else:
    print('mixed')