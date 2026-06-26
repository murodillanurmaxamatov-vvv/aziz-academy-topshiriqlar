def r(w, h=1):
    return w * h

p = list(map(int, input().split()))

if len(p) == 1:
    print(r(p[0]))
else:
    print(r(p[0], p[1]))