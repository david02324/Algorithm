n = int(input())
temp = 666
while True:
    strTemp = str(temp)
    for i in range(len(strTemp)-2):
        if strTemp [i]== '6':
            if strTemp[i+1] == '6':
                if strTemp[i+2] == '6':
                    n -= 1
                    if n == 0:
                        print(temp)
                        exit()
                    break
    
    temp += 1