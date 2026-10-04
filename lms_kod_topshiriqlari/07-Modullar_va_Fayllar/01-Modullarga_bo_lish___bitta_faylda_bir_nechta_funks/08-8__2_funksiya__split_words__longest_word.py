def w(s):
    return s.split()

def l(q):
    e = q[0]
    for i in q:
        if len(i) > len(e):
            e = i
    return e

s = input()
print(l(w(s)))