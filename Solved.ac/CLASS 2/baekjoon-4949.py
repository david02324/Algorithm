# 스택을 이용한 풀이
def balanced(string):
    stack = []
    for char in string:
        if char == '(' or char =='[':
            stack.append(char)
        elif char == ')' or char == ']':
            if stack:
                if char == ')' and stack.pop() != '(':
                    return 'no'
                elif char == ']' and stack.pop() != '[':
                    return 'no'
            else:
                return 'no'
        elif char =='.':
            if not stack:
                return 'yes'
            else:
                return 'no'

answer = []
while True:
    string = input()
    if string == '.':
        break
    answer.append(balanced(string))

print('\n'.join(answer))