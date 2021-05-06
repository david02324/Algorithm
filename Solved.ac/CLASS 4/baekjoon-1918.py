# dawitblog.tistory.com/152
stack,ans = [],[]
# 우선순위 정의
priority = {
    '*':0,
    '/':0,
    '+':1,
    '-':1
}
for char in '('+input()+')':
    # 알파벳이라면
    if char.isalpha():
        ans.append(char)

    # 여는 괄호라면 스택에 추가
    elif char == '(':
        stack.append(char)
    
    # 닫는 괄호라면 해당 괄호 안에 남은 모든 연산자 출력
    elif char == ')':
        while stack[-1] != '(':
            ans.append(stack.pop())
        stack.pop()
    
    # 연산자라면 괄호 내부의 자신보다 우선순위가 높거나 같은 연산자 출력 후 스택에 자신 추가
    else:
        while stack[-1] != '(' and priority[char] >= priority[stack[-1]]:
            ans.append(stack.pop())
        stack.append(char)

print(''.join(ans))