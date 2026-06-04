n = int(input())
s = list(map(int,input().split()))
maks = s[0]
index = 0
for i in range(1, n):
    if s[i] > maks:
        maks = s[i]
        index = i
        
print(index)