l = []

def a(m):
    l.append(m)
    
n = int(input())

for _ in range(n):
    m = input()
    a(m)
    
print(len(l))
for i in l:
    print(i)