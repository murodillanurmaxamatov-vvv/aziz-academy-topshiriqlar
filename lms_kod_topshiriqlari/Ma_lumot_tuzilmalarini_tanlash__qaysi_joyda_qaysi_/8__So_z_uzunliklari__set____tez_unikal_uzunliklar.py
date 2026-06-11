w = input().split()

l = set(len(i) for i in w)

print(*sorted(l))