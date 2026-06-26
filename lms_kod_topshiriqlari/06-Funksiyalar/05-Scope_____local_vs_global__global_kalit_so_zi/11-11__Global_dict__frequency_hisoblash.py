f = {}

def a(w):
    w = w.lower()
    if w in f:
        f[w] += 1
    else:
        f[w] = 1
        
n = int(input())
for _ in range(n):
    word = input().strip()
    a(word)
    
for word in sorted(f):
    print(word, f[word])