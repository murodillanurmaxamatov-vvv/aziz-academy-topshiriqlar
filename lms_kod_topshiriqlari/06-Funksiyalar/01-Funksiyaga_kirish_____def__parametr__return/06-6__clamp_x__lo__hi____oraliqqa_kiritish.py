def A(x, y, c):
    if x < y:
        return y
    elif x > c:
        return c
    else:
        return x
    
x, y, c = map(int, input().split())
print(A(x, y, c))