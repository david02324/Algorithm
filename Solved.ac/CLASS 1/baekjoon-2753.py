n=int(input())
print(int((not n%4 and n%100!=0) or not n%400))