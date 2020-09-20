#URI Online Judge - Exercise Number 1012

def triangulo(A, C):
    print ("TRIANGULO: %.3f" %((A * C) / 2))

def circulo(C):
    pi = 3.14159
    print ("CIRCULO: %.3f" %(pi * C * C))

def trapezio(A, B, C):
    print ("TRAPEZIO: %.3f" %(((A + B) * C) / 2))

def quadrado(B):
    print ("QUADRADO: %.3f" %(B * B))

def retangulo(A, B):
    print ("RETANGULO: %.3f" %(A * B))
        
A, B, C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)

triangulo(A, C)
circulo(C)
trapezio(A, B, C)
quadrado(B)
retangulo(A, B)
