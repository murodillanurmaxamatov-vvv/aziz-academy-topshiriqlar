def c(t):
    v = "aeiou"
    x = 0
    for i in t.lower():
        if i in v:
            x += 1
    return x

def z(t):
    b = "qwrtypsdfghjklzxcvbnm"
    x = 0
    for i in t.lower():
        if i in b:
            x += 1
    return x

t = input()

print(c(t))
print(z(t))