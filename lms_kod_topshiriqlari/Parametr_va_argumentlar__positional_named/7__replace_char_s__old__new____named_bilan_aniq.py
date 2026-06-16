def ch(s, old, new):
    return s.replace(old, new)

s = input().strip()
old = input().strip()
new = input().strip()

print(ch(s, old, new))
print(ch(new=new, s=s, old=old))