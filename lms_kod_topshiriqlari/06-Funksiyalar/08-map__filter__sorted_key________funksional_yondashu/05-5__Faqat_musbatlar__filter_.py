a = list(map(int, input().split()))
toq = list(filter(lambda x: x>  0, a))
print(*toq)