import math

def mean(nu):
    return sum(nu) / len(nu)

def va(nu):
    m = mean(nu)
    jami = 0
    for i in nu:
        jami += (i - m) ** 2
    return jami / len(nu)

def std(nu):
    return math.sqrt(va(nu))

nu = list(map(int, input().split()))
print(f"{mean(nu):.2f}")
print(f"{va(nu):.2f}")
print(f"{std(nu):.2f}")