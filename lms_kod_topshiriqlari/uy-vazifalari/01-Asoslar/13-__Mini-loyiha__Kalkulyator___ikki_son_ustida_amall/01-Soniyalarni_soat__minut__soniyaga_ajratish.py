x = int(input())
s = x // 3600
m = (x % 3600) // 60
c = x % 60
print(s)
print(m)
print(c)