n = list(map(int,input().split()))

stats = {
    'count': len(n),
    'sum': sum(n),
    'min': min(n),
    'max': max(n)
}
print(stats)