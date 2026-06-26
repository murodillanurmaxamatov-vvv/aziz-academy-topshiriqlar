def d(a):
    return {
        'count': len(a),
        'sum': sum(a),
        'min': min(a),
        'max': max(a)
    }
    
a = list(map(int, input().split()))
print(d(a))