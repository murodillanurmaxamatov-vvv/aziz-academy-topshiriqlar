a, b, c = input().split()

def conv(x):
    if x.isdigit():
        return int(x)
    try:
        return float(x)
    except:
        return x
print((conv(a), conv(b), conv(c)))