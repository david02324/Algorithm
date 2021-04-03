def makeLi(s):
    result = []
    
    for i in range(0,len(s)-1):
        cur = s[i:i+2]
        if (cur.isalpha()):
            result.append(cur)
    
    return result

def solution(str1, str2):
    li1 = makeLi(str1.lower())
    li2 = makeLi(str2.lower())
    
    common = []
    for i in set(li1) & set(li2):
        for _ in range(min(li1.count(i),li2.count(i))):
            common.append(i)
            
    sum_set = []
    for i in set(li1) | set(li2):
        for _ in range(max(li1.count(i),li2.count(i))):
            sum_set.append(i)
            
    if not li1 and not li2:
        answer = 1
    else:
        answer = len(common) / len(sum_set)
        
    return int(answer * 65536)