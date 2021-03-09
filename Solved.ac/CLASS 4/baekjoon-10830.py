# dawitblog.tistory.com/161
from sys import stdin
input = stdin.readline

# 행렬 곱셈
def mat_multi(a,b):
    temp = [[0]*size for _ in range(size)]

    for r in range(size):
        for c in range(size):
            for k in range(size):
                temp[r][c] += a[r][k] * b[k][c]

    for r in range(size):
        for c in range(size):
            temp[r][c] %= 1000

    return temp


size, count = map(int,input().split())
mat = []
for _ in range(size):
    mat.append(list(map(int,input().split())))

# 단위 행렬
ans_mat = [[int(r==c) for c in range(size)] for r in range(size)]

# 분할 정복
while count != 1:
    if count % 2:
        ans_mat = mat_multi(ans_mat,mat)
        count -= 1
    else:
        mat = mat_multi(mat,mat)
        count //= 2

ans_mat = mat_multi(ans_mat,mat)
# 출력
for line in ans_mat:
    print(*line)