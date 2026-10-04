def p(l):
    return [int(x) for x in l.split()]

def u(n):
    return list(set(n))

def s(n):
    return sorted(n)

n = s(u(p(input())))
print(" ".join(str(x) for x in n))