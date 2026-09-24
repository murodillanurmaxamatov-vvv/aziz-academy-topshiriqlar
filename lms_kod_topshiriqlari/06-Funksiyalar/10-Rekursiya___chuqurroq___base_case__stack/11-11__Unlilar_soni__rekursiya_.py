def v(s):
    if s == "":
        return 0
    
    c = "aeiou"
    
    e = 1 if s[0] in c else 0
    
    return e + v(s[1:])

s = input().strip()
print(v(s))