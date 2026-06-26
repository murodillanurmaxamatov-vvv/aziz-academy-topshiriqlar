def m(name, r='student'):
    return f"name={name}, role={r}"

t = input().split()

if len(t) == 1:
    print(m(t[0]))
else:
    print(m(t[0], t[1]))