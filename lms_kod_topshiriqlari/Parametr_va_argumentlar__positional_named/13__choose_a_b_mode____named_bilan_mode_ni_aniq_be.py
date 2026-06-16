def son(a, b, mode):
    if mode == "max":
        return max(a, b)
    elif mode == "min":
        return min(a, b)
    return a

a, b = map(int, input().split())
mode = input().strip()

print(son(a, b, mode))
print(son(mode=mode, a=a, b=b))