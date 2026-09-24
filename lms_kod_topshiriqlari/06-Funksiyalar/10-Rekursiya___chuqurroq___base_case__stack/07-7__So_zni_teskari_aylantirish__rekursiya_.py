def r(s):
    if len(s) <= 1:
        return s
    return s[-1] + r(s[:-1])

s = input().strip()
print(r(s))