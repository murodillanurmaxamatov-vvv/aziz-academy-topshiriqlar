def l(ch='-', n=10):
    return ch * n

t = input().split()

if len(t) == 0:
    print(l())
elif len(t) == 1:
    if t[0].lstrip('-').isdigit():
        print(l(n=int(t[0])))
    else:
        print(l(ch=t[0]))
else:
    print(l(t[0], int(t[1])))
        