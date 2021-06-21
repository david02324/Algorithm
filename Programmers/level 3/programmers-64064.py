result_li = []

def check(user,banned):
    if len(user) != len(banned):
        return False

    for i in range(len(user)):
        if banned[i] != '*' and user[i] != banned[i]:
            return False

    return True

def dfs(cand_li,banned_id,idx):
    global result_li

    if idx == len(banned_id):
        if set(cand_li) not in result_li:
            result_li.append(set(cand_li))
        return

    for i in range(len(cand_li)):
        if check(cand_li[i],banned_id[idx]):
            temp = cand_li.pop(i)
            dfs(cand_li,banned_id,idx+1)
            cand_li.insert(i,temp)

def solution(user_id, banned_id):
    global result_li
    cand_set = set()

    for banned in banned_id:
        for user in user_id:
            if check(user,banned):
                cand_set.add(user)

    cand_li = list(cand_set)

    dfs(cand_li,banned_id,0)
    
    return len(result_li)