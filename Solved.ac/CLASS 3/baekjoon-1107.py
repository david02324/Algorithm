# dawitblog.tistory.com
# 브루트포스
ch,m = int(input()),int(input())
count = abs(100-ch)
if m:
    l = input().split()
    # 고장난 버튼 빼고 누를 수 있는 버튼
    available = [str(k) for k in range(10) if str(k) not in l]

    if available:
        for num in range(1000001):
            num = str(num)
            for i in range(len(num)):
                if num[i] not in available:
                    break
                elif i == len(num) - 1:
                    count = min(count,len(num) + abs(ch-int(num)))
    print(count)
else:
    print(len(str(ch)) if len(str(ch)) < count else count)