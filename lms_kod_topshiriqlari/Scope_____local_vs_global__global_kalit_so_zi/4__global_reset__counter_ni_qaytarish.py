c = 0

def inc():
    global c
    c += 1
    return c

def reset():
    global c
    c = 0
    return 0

q = int(input())

for _ in range(q):
    d = input().strip()
    
    if d == 'inc':
        print(inc())
    else:
        print(reset())