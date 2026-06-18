def c(a, b=1, o='+'):
    if o == '+':
        return a + b
    if o == '-':
        return a - b
    if o == '*':
        return a * b
    if o == '/':
        if b == 0:
            return "ERROR"
        return a / b
    
t = input().split()
a = int(t[0])
b = 1
o = '+'

if len(t) == 2:
    b = int(t[1])
elif len(t) == 3:
    b =int(t[1])
    o = t[2]
    
res = c(a, b, o)

if res == "ERROR":
    print('ERROR')
else:
    if isinstance(res, float) and res != int(res):
        print(f"{res:.2f}")
    else:
        print(int(res))