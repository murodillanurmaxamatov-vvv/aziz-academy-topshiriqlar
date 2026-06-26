def j(*args, sep='-'):
    return sep.join(args)

sep = input()
s = input().split()

print(j(*s, sep=sep))