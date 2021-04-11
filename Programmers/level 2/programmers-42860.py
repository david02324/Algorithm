def find_shortest_distance(s):
    distance_list = [len(s)-1]
    
    pos = 0
    while pos < len(s):
        if s[pos] == 'A':
            distance_list.append(pos-1)
            pos += 1
            count = 1
            while pos < len(s) and s[pos] == 'A':
                pos += 1
                count += 1
            distance_list[-1] += len(s) - count - 1
        else:
            pos += 1
            
    return min(distance_list)
                

def solution(name):
    ud_cost = sum([min(ord(char)-ord('A'),ord('Z')-ord(char)+1) for char in name])
    
    return ud_cost + find_shortest_distance(name)