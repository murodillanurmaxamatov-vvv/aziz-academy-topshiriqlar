def p(s):
    return "Ha" if s == s[::-1] else "Yo'q"

s = input()
print(p(s))