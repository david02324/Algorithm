n, r, c = map(int, input().split())
num = 0
while n > 0:
    # 최대크기의 1/4 의 정사각형
    temp = (2 ** (n-1))
    if n >= 1:
        # 좌하단
        if r < temp and c >= temp:
            num += temp ** 2
            c -= temp
        # 우상단
        elif r >= temp and c < temp:
            num += (temp ** 2) * 2
            r -= temp
        # 우하단
        elif r >= temp and c >= temp:
            num += (temp ** 2) * 3
            r -= temp
            c -= temp
    
    n -= 1
print(num)