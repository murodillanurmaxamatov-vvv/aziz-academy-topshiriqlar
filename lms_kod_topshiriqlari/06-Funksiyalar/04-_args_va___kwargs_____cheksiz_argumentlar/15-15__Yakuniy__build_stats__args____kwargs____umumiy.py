def b(*args, **kwargs):
    return {
        'count': len(args),
        'min': min(args),
        'max': max(args),
        'sum': sum(args),
        'extra_keys': sorted(kwargs.keys()),
        'extra_sum': sum(kwargs.values())
    }
    
args = list(map(int, input().split()))
n = int(input())

d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
    
print(b(*args, **d))