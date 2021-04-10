def solution(s):
    li = s.lstrip('{').rstrip('}').split('},{')
    
    if len(li) == 1:
        return [int(s[2:-2])]
    
    position = [-1] * len(li)
    for i in range(len(li)):
        li[i] = set(map(int,li[i].split(',')))
        position[len(li[i])-1] = i
    
    answer = [0] * len(li)
    prev = set()
    for i in range(len(li)):
        answer[i] = list(li[position[i]] - prev)[0]
        prev = li[position[i]]
    
    return answer