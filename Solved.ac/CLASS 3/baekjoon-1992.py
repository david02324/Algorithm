# dawitblog.tistory.com
from sys import stdin
input = stdin.readline

video = [list(input()) for _ in range(int(input()))]

def yaho(video,startR,startC,n):
    global answer
    # 1X1 정사각형까지 분할되었을 경우
    if n == 1:
        answer += video[startR][startC]
        return

    # 좌상단 기억
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