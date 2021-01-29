# 재귀(재귀스택 초과)
# n = int(input())

# def find(n):
#     countList = []
#     if n == 1:
#         return 0
    
#     countList.append(find(n-1) + 1)
#     if n % 3 == 0:
#         countList.append(find(n//3) + 1)
#     if n % 2 == 0:
#         countList.append(find(n//2) + 1)

#     return min(countList)

# print(find(n))

cache = set([int(input())])
count = 0
while True:
    temp = cache.copy()
    for i in temp:
        if i == 1:
            print(count)
            exit()
        
        cache.add(i-1)
        if i % 3 == 0:
            cache.add(i//3)
        if i % 2 == 0:
            cache.add(i//2)

    cache -= temp  
    count += 1