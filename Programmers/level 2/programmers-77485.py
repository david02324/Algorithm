def solution(rows, columns, queries):
    board = [[c for c in range(r*columns+1,(r+1)*columns+1)] for r in range(rows)]
    
    ans = []
    for r1,c1,r2,c2 in queries:
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        
        min_value = min(min(board[r1][c1:c2+1]),min(board[r2][c1:c2+1]))
        for r in range(r1,r2+1):
            min_value = min(min_value,board[r][c1],board[r][c2])
        
        ans.append(min_value)
        
        board[r1].insert(c1,board[r1].pop(c2))
        board[r2].insert(c2,board[r2].pop(c1))
        temp1 = board[r2][c2]
        temp2 = board[r1][c1]
        
        for r in range(r2,r1,-1):
            board[r][c2] = board[r-1][c2]
        for r in range(r1,r2):
            board[r][c1] = board[r+1][c1]
            
        board[r2-1][c1] = temp1
        board[r1+1][c2] = temp2
        
    return ans