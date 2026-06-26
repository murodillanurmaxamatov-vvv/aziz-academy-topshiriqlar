n = int(input())
s = list(map(int,input().split()))
maks = s[0]
m = s[0]
for i in s[1:]:
    if i > maks:
        maks = i
    if i < m:
        m = i
print(maks, m)