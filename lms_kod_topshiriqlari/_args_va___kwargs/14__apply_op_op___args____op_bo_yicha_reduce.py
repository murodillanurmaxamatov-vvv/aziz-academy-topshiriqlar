def a(op, *args):
    if op == 'sum':
        return sum(args)
    else:
        p = 1
        for x in args:
            p *= x
        return p
    
op = input().split()
y = list(map(int, input().split()))

print(a(op, *y))