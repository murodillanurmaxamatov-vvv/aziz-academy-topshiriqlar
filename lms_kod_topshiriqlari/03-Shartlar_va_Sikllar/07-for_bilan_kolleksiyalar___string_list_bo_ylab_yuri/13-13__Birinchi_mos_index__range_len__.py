n = int(input())
s = list(map(int,input().split()))
x = int(input())
index = -1
for i in range(len(s)):
    if s[i] == x:
        index = i
        break
print(index)