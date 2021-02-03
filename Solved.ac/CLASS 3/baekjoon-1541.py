f = input()
li = [char for char in f]

# 첫번째항 0 제거
while li[0] == '0':
    del li[0]

# 이후 항의 쓸모없는 0 제거
i = 1
while i < len(li):
    if li[i] == '0' and not li[i-1].isdigit():
        del li[i]
    else:
        i += 1

# 괄호 추가
i = 0
isOpen = False
while i < len(li):
    if li[i] == '-' and not isOpen:
        li.insert(i+1,'(')
        isOpen = True
    elif li[i] == '-' and isOpen:
        li.insert(i,')')
        isOpen = False

    i += 1

# 마지막에 괄호 닫지 않았을 시 닫기
if isOpen:
    li.append(')')

print(eval(''.join(li)))