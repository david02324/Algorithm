import sys
input = sys.stdin.readline
coords = [input() for _ in range(int(input()))]
coords = sorted(coords, key=lambda coord: (int(coord.split()[1]),int(coord.split()[0])))

print(''.join(coords))