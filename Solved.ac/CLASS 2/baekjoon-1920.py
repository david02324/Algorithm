import sys
input = sys.stdin.readline
n,numbers,m = input(),set(input().split()),input()
for number in input().split():
    print(int(number in numbers))