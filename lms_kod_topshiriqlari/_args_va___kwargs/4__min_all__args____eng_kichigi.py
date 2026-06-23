def son(*args):
    return min(*args)

a = list(map(int, input().split()))
print(son(a))