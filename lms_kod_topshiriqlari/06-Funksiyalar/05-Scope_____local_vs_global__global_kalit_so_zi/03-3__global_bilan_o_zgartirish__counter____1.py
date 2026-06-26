c = 0

def inc():
    global c
    c += 1
    return c

n = int(input())

for _ in range(n):
    print(inc())