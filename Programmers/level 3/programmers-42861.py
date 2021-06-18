def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    connected = [i for i in range(n)]
    totalCost = 0
    
    while len(set(connected)) != 1:
        a,b,cost = costs.pop(0)
        # 연결되지 않은 노드라면
        if connected[a] != connected[b]:
            temp = connected[b]
            # 모든 노드에 대해
            for i in range(n):
                # b와 같은 값을 가진 노드를
                if connected[i] == temp:
                    # 모두 a로 변경
                    connected[i] = connected[a]
            # 코스트 누적
            totalCost += cost
    
    return totalCost