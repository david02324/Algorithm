from itertools import combinations

def solution(relation):
    n = len(relation)
    c = len(relation[0])
    
    candidates = []
    for count in range(1,n):
        li = list(combinations(range(c),count))
        
        for cols in li:
            temp_set = set()
            for tup in relation:
                temp_tup = tuple([tup[idx] for idx in cols])
                if temp_tup in temp_set:
                    break
                else:
                    temp_set.add(temp_tup)
            else:
                for candidate in candidates:
                    if candidate.issubset(set(cols)):
                        break
                else:
                    candidates.append(set(cols))
                
    return len(candidates)