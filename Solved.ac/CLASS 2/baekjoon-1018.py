N,M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
countList = []

for startingLine in range(N-7):
    for startingCol in range(M-7):
        count = 0

        for line in range(startingLine,startingLine+8):
            for col in range(startingCol,startingCol+8):
                if (line+col) % 2 == 0:
                    if board[line][col] != 'B':
                        count += 1
                else:
                    if board[line][col] != 'W':
                        count += 1
        
        countList.append(count)

for i in range(len(countList)):
    case1 = countList[i]
    case2 = 64 - case1
    countList.append(case2)

print(min(countList))