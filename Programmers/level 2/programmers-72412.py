from bisect import bisect_left,insort

def change(s):
    if s == '-':
        return 0
    
    if s == 'cpp' or s == 'backend' or s == 'junior' or s == 'chicken':
        return 1
    
    if s == 'java' or s == 'frontend' or s == 'senior' or s == 'pizza':
        return 2
    
    if s == 'python':
        return 3
    

def solution(info, query):
    db = [[] for _ in range(4)]
    for i in range(4):
        db[i] = [[] for _ in range(3)]
        for j in range(3):
            db[i][j] = [[] for _ in range(3)]
            for k in range(3):
                db[i][j][k] = [[] for _ in range(3)]
    
    for row in info:
        row_data = row.split()
        score = int(row_data.pop())
        
        for i in range(4):
            row_data[i] = change(row_data[i])
        
        for c1 in (0,row_data[0]):
            for c2 in (0,row_data[1]):
                for c3 in (0,row_data[2]):
                    for c4 in (0,row_data[3]):
                        insort(db[c1][c2][c3][c4],score)
    
    ans = []
    for cmd in query:
        cmd = cmd.split(' and ')
        cmd += cmd.pop().split()
        score = int(cmd.pop())
        
        cmd = list(map(change,cmd))

        count = len(db[cmd[0]][cmd[1]][cmd[2]][cmd[3]]) - bisect_left(db[cmd[0]][cmd[1]][cmd[2]][cmd[3]],score)
        
        ans.append(count)
    return ans