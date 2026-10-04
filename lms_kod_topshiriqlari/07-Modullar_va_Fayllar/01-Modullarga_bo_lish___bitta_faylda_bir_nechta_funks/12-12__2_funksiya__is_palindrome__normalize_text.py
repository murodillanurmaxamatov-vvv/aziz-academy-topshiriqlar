def n(s):
    toza = ""
    for i in s.lower():
        if i.isalpha():
            toza += i
    return toza

def i(s):
    t = n(s)
    return t == t[::-1]

s = input()
print(i(s))