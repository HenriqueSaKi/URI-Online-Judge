#URI Online Judge - Exercise Number 1013

def maior(a, b):
    if(a>b):
        return a
    else:
        return b

x, y, z = input().split(" ")
x = int(x)
y = int(y)
z = int(z)

print ("%i eh o maior" %(maior(maior(x,y),z))) 
