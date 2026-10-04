def di(n):
    jami = 0
    for i in str(n):
        jami += int(i)
    return jami

def dc(n):
    return len(str(n))

def dr(n):
    return int(str(n)[::-1])

n = int(input())
print(di(n))
print(dc(n))
print(dr(n))