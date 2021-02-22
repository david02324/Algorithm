l = input().split()
print(l[0][::-1] if int(l[0][::-1]) > int(l[1][::-1]) else l[1][::-1])