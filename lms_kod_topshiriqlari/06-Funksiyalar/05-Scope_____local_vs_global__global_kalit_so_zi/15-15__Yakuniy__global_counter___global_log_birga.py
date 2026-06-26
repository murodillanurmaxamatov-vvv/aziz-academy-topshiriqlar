c = 0
l = []

def add(m):
    global c
    l.append(m)
    c += 1

def s():
    return "count=" + str(c) + ', logs=' + str(len(l))

n = int(input())

for _ in range(n):
    add(input())
    
    
print(s())