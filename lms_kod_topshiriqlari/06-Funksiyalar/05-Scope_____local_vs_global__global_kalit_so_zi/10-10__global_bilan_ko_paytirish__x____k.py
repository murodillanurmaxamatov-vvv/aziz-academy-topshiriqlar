x = 2

def m(k):
    global x
    x *= k
    return x

n = int(input())
for _ in range(n):
    k = int(input())
    print(m(k))