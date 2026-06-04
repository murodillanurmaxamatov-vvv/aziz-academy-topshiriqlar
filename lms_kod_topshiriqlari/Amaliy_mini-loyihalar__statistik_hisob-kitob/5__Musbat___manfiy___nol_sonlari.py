x = list(map(int,input().split()))

a = 0
b = 0
c = 0
for i in x:
    if i > 0:
        a += 1
    elif i < 0:
        b += 1
    elif i == 0:
        c += 1
        
print(a)
print(b)
print(c)