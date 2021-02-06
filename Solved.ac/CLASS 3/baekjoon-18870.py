# dawitblog.tistory.com
input()
# 입력 저장
li = list(map(int,input().split()))
# 정렬
srtLi = sorted(li)
# 해당 좌표의 압축값을 저장할 dict
di = {}

count = 0
di[srtLi[0]] = 0
for i in range(1,len(srtLi)):
    if srtLi[i] > srtLi[i-1]:
        count += 1

    di[srtLi[i]] = count

for num in li:
    print(di[num],end=' ')