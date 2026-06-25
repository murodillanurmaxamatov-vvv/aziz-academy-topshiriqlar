n = []

def p(x):
    n.append(x)
    
def l():
    if len(n) == 0:
        return 'NONE'
    return n[-1]

q = int(input())

for _ in range(q):
    c = input().split()
    
    if c[0] == 'push':
        p(int(c[1]))
    elif c[0] == 'last':
        print(l())