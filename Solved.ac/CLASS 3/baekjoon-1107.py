# # dawitblog.tistory.com
# ch,_,l = input(),input(),input().split()

# # 고장난 버튼 빼고 누를 수 있는 버튼
# available = [str(k) for k in range(10) if str(k) not in l]
# # 버튼이 모두 고장났다면 그냥 +,- 만으로 이동
# if not available:
#     print(abs(100 - int(ch)))
# else:
#     # 현재 결정해야 하는 자릿수
#     cipher = 0
#     # 해당 자릿수의 수
#     c = int(ch[cipher])
#     # 버튼으로 갈 수 있는 답에 가장 가까운 수
#     s = ''
#     # 아직 s를 모두 만들지 못했다면
#     while len(s) < len(ch):
#         for i in range(len(available)):
#             # 더 큰 수의 버튼만 사용 가능하다면
#             if int(available[0]) > c:
#                 # 나머지를 모두 최소 숫자로만 구성
#                 s += available[0]*(len(ch)-len(s))
#                 break
#             # 더 작은 수의 버튼만 사용 가능하다면
#             if int(available[-1]) < c:
#                 # 나머지를 모두 최대 숫자로만 구성
#                 s += available[-1]*(len(ch)-len(s))
#                 break
#             # 해당 수와 같은 버튼을 사용할 수 있다면
#             if int(available[i]) == c:
#                 elif int(ch[cipher+1])>=5 and c+1 == int(available[i+1]):
#                     s += available[i+1]
#                 else:
#                     # 해당 수 추가 후 다음 자릿수 검사
#                     s += available[i]
#                     cipher += 1
#                     c = int(ch[cipher])
#                 break
#             # 더 큰 수의 버튼이 사용 가능하다면
#             if int(available[i]) > c:
#                 # 남은 자릿수 만큼을 구성
#                 smaller = s + available[i-1] + available[-1]*(len(ch)-len(s)-1)
#                 bigger = s + available[i] + available[0]*(len(ch)-len(s)-1)
#                 # 채널보다 더 큰 수와 작은 수 중 더 가까운 수를 선택
#                 s = smaller if int(ch)-int(smaller)<int(bigger)-int(ch) else bigger
#                 break

#     count = len(s) + abs(int(s)-int(ch))
#     # +,-만 써서 가는 횟수와 구한 수부터 가는 횟수 중 작은 것을 출력            
#     print(count if count < abs(100-int(ch)) else abs(100-int(ch)))

ch,_,l = int(input()),input(),input().split()

# 고장난 버튼 빼고 누를 수 있는 버튼
available = [str(k) for k in range(10) if str(k) not in l]

count = abs(100-ch)
if available:
    for num in range(1000001):
        num = str(num)
        for i in range(len(num)):
            if num[i] not in available:
                break
            elif i == len(num) - 1:
                count = min(count,len(num) + abs(ch-int(num)))
print(count)