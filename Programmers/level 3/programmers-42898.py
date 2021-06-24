def solution(m, n, puddles):
    mat = [[0]*(m+1) for _ in range(n+1)]
    
    mat[1][1] = 1
    for r,c in puddles:
        mat[c][r] = -1
    
    for r in range(1,n+1):
        for c in range(1,m+1):
            if mat[r][c] != -1:
                if mat[r-1][c] != -1:
                    mat[r][c] += mat[r-1][c]
                if mat[r][c-1] != -1:
                    mat[r][c] += mat[r][c-1]
    
    return mat[r][c] % 1000000007