import sys
input = sys.stdin.readline
people = []
for _ in range(int(input())):
    temp = input().split()
    age = int(temp[0])
    name = temp[1]
    people.append((age,name))

people = sorted(people, key=lambda person: person[0])

for person in people:
    print(str(person[0]) + " " + person[1])