d = [1, 2, 3]

def c():
    global d
    d = []
    
c()
print(len(d))