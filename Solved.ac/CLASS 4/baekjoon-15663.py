# dawitblog.tistory.com
def comb(length):
    if length == m:
        temp = len(resultList)
        resultList.add(tuple(result))
        if temp != len(resultList):
            print(*result)
    else:
        for i in range(n):
            if not used[i]:
                used[i] = True
                result.append(l[i])
                comb(length+1)
                result.pop()
                used[i] = False

n, m = map(int,input().split())
# 각각의 결과를 임시로 저장
result = []
# 이미 사용한 인덱스 확인용
used = [False] * n
# 이미 출력한 결과
resultList = set()
l = sorted(list(map(int,input().split())))
comb(0)