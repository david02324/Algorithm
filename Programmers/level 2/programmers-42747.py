def solution(citations):
    citations.sort(reverse=True)
    
    for h in range(len(citations)):
        if citations[h] < h+1:
            return h
    
    return len(citations)