def t(s):
    if s == "":
        return 0
    return 1 + t(s[1:])

s = input().strip()

print(t(s))