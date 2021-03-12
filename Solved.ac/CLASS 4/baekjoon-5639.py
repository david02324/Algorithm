# dawitblog.tistory.com
import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

def postOrder(l,r):
    if l > r:
        return
    
    div = r + 1
    for i in range(l+1,r+1):
        if values[l] < values[i]:
            div = i
            break

    postOrder(l+1,div-1)
    postOrder(div,r)
    ans.append(values[l])

values = []
ans = []
# 입력
while True:
    try:
        values.append(int(input()))
    except:
        break

postOrder(0,len(values)-1)
print('\n'.join(map(str,ans)))