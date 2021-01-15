testNum = int(input())
answerList = []
for _ in range(testNum):
    h,w,n = map(int,input().split())
    countH = 0
    countW = 1
    for i in range(n):
        if(countH == h):
            countH = 1
            countW+= 1
            continue

        countH+=1
    
    answerStr = str(countH)
    if(countW < 10):
        answerStr += '0'
    answerStr += str(countW)

    answerList.append(answerStr)

for roomNum in answerList:
    print(roomNum)