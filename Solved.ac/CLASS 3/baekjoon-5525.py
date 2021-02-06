# dawitblog.tistory.com
n,m,s = int(input()),int(input()),input()

ls = list(s)
# 직전에 뽑은 글자가 O였는지 확인
wasO = True
# 2회 이전에 I가 있었는지 확인
isOpen = False
tempCount = 0
realCount = 0
while ls:
    char = ls.pop()
    # I를 뽑았는데 직전이 O였다면
    if char == 'I' and wasO:
        wasO = False
        # 2회 이전에 I가 있었다면
        if isOpen:
            tempCount += 1
        else:
            isOpen = True
    # O를 뽑았는데 직전에 O가 아니었다면(I였다면)
    elif char == 'O' and not wasO:
        wasO = True
    # 규칙이 깨졌다면
    else:
        # 1회 이상의 Pn을 만들었다면
        if tempCount != 0:
            # n회 이상의 패턴이 연속되었다면
            if tempCount - n >= 0:
                realCount += tempCount - n + 1
            tempCount = 0
        # OO의 형태로 끝났다면
        if char == 'O':
            isOpen = False

if tempCount - n >= 0:
    realCount += tempCount - n + 1

print(realCount)