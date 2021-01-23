import sys
input = sys.stdin.readline
coords = [input() for _ in range(int(input()))]
coords = sorted(coords, key=lambda coord: (int(coord.split()[0]),int(coord.split()[1])))

print(''.join(coords))