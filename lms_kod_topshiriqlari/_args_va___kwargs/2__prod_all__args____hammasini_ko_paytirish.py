def kop(*args):
    p = 1
    for i in args:
        p *= i
    return p

a = list(map(int, input().split()))

print(kop(*a))