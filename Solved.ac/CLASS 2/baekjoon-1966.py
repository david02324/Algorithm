import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    queue = list(map(int,input().split()))

    # 몇 번째 출력인지를 알기 위한 count변수
    count = 0
    while True:
        # 중요도가 가장 크지 않은 문서의 경우 뒤로 넘김
        if max(queue) > queue[0]:
            queue.append(queue.pop(0))
            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1
        # 중요도가 가장 큰 문서일 경우 출력
        else:
            queue.pop(0)
            count += 1
            if m == 0:
                print(count)
                break
            else:
                m -= 1