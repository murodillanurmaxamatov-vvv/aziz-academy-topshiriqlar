def t(s):
    if len(s) <= 1:
        return s
    return s[-1] + t(s[:-1])

n = input().strip()
print(t(n))