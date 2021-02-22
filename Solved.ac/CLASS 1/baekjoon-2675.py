for _ in range(int(input())):
    l=input().split()

    ans = ''
    n=int(l[0])
    for char in l[1]:
        ans += char*n
    print(ans)