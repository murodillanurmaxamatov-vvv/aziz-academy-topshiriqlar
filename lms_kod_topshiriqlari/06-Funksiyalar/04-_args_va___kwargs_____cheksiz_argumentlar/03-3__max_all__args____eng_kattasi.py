def son(*args):
    return max(*args)

a = list(map(int, input().split()))
print(son(a))