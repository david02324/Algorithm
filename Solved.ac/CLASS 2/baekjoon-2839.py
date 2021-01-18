def find(N):
    for five in range(N // 5,-1,-1):
        for three in range(N // 3 + 1):
            sum = three*3 + five*5
            if(sum == N):
                return three+five
            elif(sum > N):
                break
    return -1

print(find(int(input())))