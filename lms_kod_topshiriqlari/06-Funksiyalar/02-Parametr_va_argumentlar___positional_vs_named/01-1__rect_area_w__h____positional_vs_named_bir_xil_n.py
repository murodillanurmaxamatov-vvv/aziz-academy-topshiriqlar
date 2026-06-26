def r(w, h):
    return w * h

w, h = map(int, input().split())

print(r(w, h))
print(r(h=h, w=w))