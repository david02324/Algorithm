# dawitblog.tistory.com
def find(r):
    global count
    if r == n:
        # n줄 까지 도달했다면 1가지 경우 추가
        count += 1
        return
    for c in range(n):
        # 대각선 값
        s = r + c
        b = r - c
        if col[c] and slash[s] and backSlash[b]:
            col[c] = slash[s] = backSlash[b] = False
            find(r+1)
            col[c] = slash[s] = backSlash[b] = True

n = int(input())
col = [True] * n
slash = [True] * (n*2+1)
backSlash = [True] * (n*2+1)
count = 0
find(0)
print(count)