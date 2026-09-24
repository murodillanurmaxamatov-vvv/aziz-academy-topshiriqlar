def pp(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return pp(s[1:-1])

s = input().strip()
if pp(s):
    print("Ha")
else:
    print("Yo'q")