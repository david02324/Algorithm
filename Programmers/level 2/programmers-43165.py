count = 0
def dfs(arr,info):
    global count
    if len(arr) == info[0]:
        if sum(arr) == info[2]:
            count += 1
        return

    arr.append(info[1][len(arr)])
    dfs(arr,info)
    arr.pop()

    arr.append(-info[1][len(arr)])
    dfs(arr,info)
    arr.pop()


def solution(numbers, target):
    global count
    info = []
    info.append(len(numbers))
    info.append(numbers)
    info.append(target)
    dfs([],info)

    return count