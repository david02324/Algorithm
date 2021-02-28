# dawitblog.tistory.com
def comb(length,startIdx):
    if length == m:
        temp = len(resultList)
        resultList.add(tuple(result))
        if temp != len(resultList):
            print(*result)
    else:
        for i in range(startIdx,n):
                result.append(l[i])
                comb(length+1,i)
                result.pop()

n, m = map(int,input().split())
# 각각의 결과를 임시로 저장
result = []
# 이미 출력한 결과
resultList = set()
l = sorted(list(map(int,input().split())))
comb(0,0)