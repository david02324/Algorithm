from collections import Counter
from itertools import combinations

def solution(orders, course):
    ans = []
    for l in course:
        li = []
        for order in orders:
            li += list(combinations(sorted(order),l))
        counter = Counter(li)
        
        if counter:
            max_ordered = max(counter.values())
            if max_ordered == 1:
                break
        else:
            break
        ans += [''.join(obj) for obj in counter if counter[obj] == max_ordered]
        
    return sorted(ans)