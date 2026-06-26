n = int(input())
s = list(map(int,input().split()))
orta = sum(s) / n
count = 0
for i in s:
    if i > orta:
        count += 1
print(count)