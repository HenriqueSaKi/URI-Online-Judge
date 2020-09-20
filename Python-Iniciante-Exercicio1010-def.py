#URI Online Judge - Exercise Number 1010 (Using "def")

def transformation(x,y,z):
    x = int(x)
    y = int(y)
    z = float(z)
    value = float(y * z)
    return value

x1,y1,z1 = input().split(" ")
value1 = transformation(x1,y1,z1)

x2,y2,z2 = input().split(" ")
value2 = transformation(x2,y2,z2)

total = value1 + value2
print ("VALOR A PAGAR: R$ %.2f" %(total))
