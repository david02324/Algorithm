from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    sticker = []

    length = int(input())
    sticker.append(list(map(int,input().split())))
    sticker.append(list(map(int,input().split())))

    cache = [[sticker[0][0],sticker[1][0]+sticker[0][1]],[sticker[1][0],sticker[0][0]+sticker[1][1]]]

    for i in range(2,length):
        cache[0].append(max(cache[1][i-2],cache[1][i-1])+sticker[0][i])
        cache[1].append(max(cache[0][i-2],cache[0][i-1])+sticker[1][i])
    
    print(max(cache[0][-1],cache[1][-1]))