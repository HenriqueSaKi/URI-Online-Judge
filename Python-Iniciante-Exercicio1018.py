#URI Online Judge - Exercise Number 1018

N = int(input())

def condition(N, value):
    if(N%value>=0):
        return N/value
    else:
        return N
        
print(N)
print("%i nota(s) de R$ 100,00" %(condition(N, 100)))
print("%i nota(s) de R$ 50,00" %(condition(N%100, 50)))
print("%i nota(s) de R$ 20,00" %(condition((N%100)%50, 20)))
print("%i nota(s) de R$ 10,00" %(condition((N%50)%20, 10)))
print("%i nota(s) de R$ 5,00" %(condition((N%20)%10, 5)))
print("%i nota(s) de R$ 2,00" %(condition((N%10)%5, 2)))
print("%i nota(s) de R$ 1,00" %(condition((N%5)%2, 1)))
