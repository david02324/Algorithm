# dawitblog.tistory.com
from sys import stdin
input = stdin.readline

dic = {}
def preOrder(node):
    global answer

    answer += node
    if dic[node][0] != '.':
        preOrder(dic[node][0])
    if dic[node][1] != '.':
        preOrder(dic[node][1])

def inOrder(node):
    global answer

    if dic[node][0] != '.':
        inOrder(dic[node][0])
    answer += node
    if dic[node][1] != '.':
        inOrder(dic[node][1])

def postOrder(node):
    global answer

    if dic[node][0] != '.':
        postOrder(dic[node][0])
    if dic[node][1] != '.':
        postOrder(dic[node][1])
    answer += node

for _ in range(int(input())):
    conn = input().split()
    dic[conn[0]] = (conn[1],conn[2])

answer = ''
preOrder('A')
print(answer)

answer = ''
inOrder('A')
print(answer)

answer = ''
postOrder('A')
print(answer)