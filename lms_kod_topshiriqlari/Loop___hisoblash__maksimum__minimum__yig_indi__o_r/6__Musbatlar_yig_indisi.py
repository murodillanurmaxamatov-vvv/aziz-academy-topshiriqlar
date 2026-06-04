n = int(input())
s = list(map(int,input().split()))
yigindi = 0
for i in s:
    if i > 0:
        yigindi += i 
print(yigindi)