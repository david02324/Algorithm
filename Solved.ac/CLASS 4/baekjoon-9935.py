# dawitblog.tistory.com/159

string, explosion = input(),input()
explosion_length = len(explosion)
str_stack,explosion_stack = [],[]
str_pointer = -1

# 폭발 문자열이 하나의 문자일 경우
if len(explosion) == 1:
    string = string.replace(explosion,'')
    print(string if string else 'FRULA')
    exit()

idx_dict = {}
for i in range(explosion_length):
    idx_dict[explosion[i]] = i

for char in string:
    str_stack.append(char)
    explosion_stack.append(char)
    str_pointer += 1
    
    # 폭발 문자열의 첫 문자가 입력된 경우
    if explosion_stack[-1] == explosion[0]:
        str_pointer = 0
    # 폭발 문자열의 마지막 문자가 입력된 경우
    elif explosion_stack[-1] == explosion[-1] and str_pointer == explosion_length - 1:
        for _ in range(explosion_length):
            # 폭발 문자열 제거
            explosion_stack.pop()
            str_stack.pop()
        # 포인터 값 초기화
        if explosion_stack:
            str_pointer = idx_dict[explosion_stack[-1]]
        else:
            str_pointer = -1
    # 폭발 문자열의 중간 문자가 순서에 맞게 입력된 경우
    elif explosion_stack[-1] in explosion and len(explosion_stack) >= 2 and idx_dict[explosion_stack[-2]] + 1 == idx_dict[explosion_stack[-1]]:
        continue
    else:
        # 폭발 스택 초기화, 포인터 값 초기화
        explosion_stack = []
        str_pointer = -1
    

print(''.join(str_stack) if str_stack else 'FRULA')