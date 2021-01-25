for _ in range(int(input())):
    baskets = 0
    for char in input():
        if char == '(':
            baskets += 1
        elif char == ')':
            baskets -= 1
            if baskets < 0:
                break

    if baskets == 0:
        print('YES')
    else:
        print('NO')