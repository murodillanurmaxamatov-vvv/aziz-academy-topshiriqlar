n = int(input())
a = list(map(int,input().split()))
s = 0
for x in a:
    if x % 2 == 0:
        s += x
print(s)