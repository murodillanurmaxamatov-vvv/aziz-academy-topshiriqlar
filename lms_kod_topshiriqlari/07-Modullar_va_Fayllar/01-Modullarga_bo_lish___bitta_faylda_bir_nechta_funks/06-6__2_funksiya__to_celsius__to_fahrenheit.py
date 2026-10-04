def to(f):
    return (f- 32) * 5/9

def fa(c):
    return c * 9 / 5 + 32

m = input().strip()
t = float(input())
if m == "C":
    print(f"{to(t):.2f}")
else:
    print(f"{fa(t):.2f}")