n = int(input())
son = list(map(int,input().split()))

s = []

for i in son:
    if i > 10:
        s.append(i)
print(s)