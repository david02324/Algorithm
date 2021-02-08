from sys import stdin
input = stdin.readline

video = [list(input()) for _ in range(int(input()))]

def yaho(video,startR,startC,n):
    global answer
    if n == 1:
        answer += video[startR][startC]
        return

    zeroOrOne = video[startR][startC]
    
    for r in range(startR,startR+n):
        for c in range(startC,startC+n):
            if zeroOrOne != video[r][c]:
                answer += '('
                yaho(video,startR,startC,n//2)
                yaho(video,startR,startC + n//2,n//2)
                yaho(video,startR + n//2,startC,n//2)
                yaho(video,startR + n//2,startC + n//2,n//2)
                answer += ')'
                return

    answer += zeroOrOne

answer = ''
yaho(video,0,0,len(video))
print(answer)