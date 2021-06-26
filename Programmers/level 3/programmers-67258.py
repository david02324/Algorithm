def solution(gems):
    target = len(set(gems))
    length = len(gems)
    dic = {gems[0]: 1}
    ans = (0,length-1)
    start, end = 0,0
    
    while start < length and end < length:
        if len(dic) == target:
            if end - start < ans[1] - ans[0]:
                ans = (start,end)
            
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            
            start += 1
        
        else:
            end += 1
            if end == length:
                break
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1
                
    return [ans[0]+1,ans[1]+1]