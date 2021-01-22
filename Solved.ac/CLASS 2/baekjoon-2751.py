# 내장함수 이용
import sys
numbers = []
for i in range(int(sys.stdin.readline().rstrip())):
    numbers.append(int(sys.stdin.readline().rstrip()))
numbers.sort()
for number in numbers:
    print(number)

# 선택 정렬(시간초과)
import sys
numbers = []
for i in range(int(sys.stdin.readline().rstrip())):
    numbers.append(int(sys.stdin.readline().rstrip()))
for i in range(len(numbers)):
    minIndex = i
    for j in range(i+1,len(numbers)):
        if numbers[minIndex] > numbers[j]:
            minIndex = j
    numbers[minIndex],numbers[i] = numbers[i],numbers[minIndex]
for number in numbers:
    print(number)

# 삽입 정렬(시간초과)
import sys
numbers = []
for i in range(int(sys.stdin.readline().rstrip())):
    numbers.append(int(sys.stdin.readline().rstrip()))
for i in range(1,len(numbers)):
    for j in range(i,0,-1):
        if numbers[j-1] > numbers[j]:
            numbers[j-1],numbers[j] = numbers[j],numbers[j-1]
        else:
            break
for number in numbers:
    print(number)

# 퀵 정렬(시간 초과,Recursion Error)
import sys
numbers = []
sys.setrecursionlimit(10**9)
for i in range(int(sys.stdin.readline().rstrip())):
    numbers.append(int(sys.stdin.readline().rstrip()))
def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    tail = array[:len(array) // 2] + array[len(array) // 2 + 1:]

    leftArray = [i for i in tail if i <= pivot]
    rightArray = [i for i in tail if i > pivot]

    return quickSort(leftArray) + [pivot] + quickSort(rightArray)

numbers = quickSort(numbers)
for number in numbers:
    print(number)

# 통과
import sys
count = [False] * 2000001
for i in range(int(sys.stdin.readline())):
    count[int(sys.stdin.readline())+1000000] = True

for i in range(2000001):
    if count[i]:
        print(i-1000000)