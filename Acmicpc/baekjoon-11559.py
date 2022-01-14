from sys import stdin
input = stdin.readline

board = [list(input()) for _ in range(12)]
ans = 0

while True:
  visited = [[False]*6 for _ in range(12)]
  flag = False

  for r in range(12):
    for c in range(6):
      if not visited[r][c] and board[r][c] != '.':
        visited[r][c] = True
        color = board[r][c]

        q = [(r,c)]
        record = [(r,c)]

        while q:
          r,c = q.pop(0)

          for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = r + dr
            nc = c + dc

            if 0<=nr<12 and 0<=nc<6 and not visited[nr][nc] and board[nr][nc] == color:
              visited[nr][nc] = True
              q.append((nr,nc))
              record.append((nr,nc))
        
        if len(record) >= 4:
          flag = True
          for r,c in record:
            board[r][c] = 'X'

  for c in range(6):
    col = []
    for r in range(12):
      if board[r][c] in ['R','G','B','P','Y']:
        col.append(board[r][c])

    for r in range(11,-1,-1):
      if col:
        board[r][c] = col.pop()
      else:
        board[r][c] = '.'

  if (flag):
    ans += 1
  else:
    print(ans)
    exit()