#URI Online Judge - Exercise Number 1010

x1,y1,z1 = input().split(" ") #call 3 variables in 1 line
x1 = int(x1) #define its type
y1 = int(y1) #define its type
z1 = float(z1) #define its type

x2,y2,z2 = input().split(" ") #call 3 variables in 1 line
x2 = int(x2) #define its type
y2 = int(y2) #define its type
z2 = float(z2) #define its type

total = (y1*z1)+(y2*z2) #calculating 
print ("VALOR A PAGAR: R$ %.2f" %(total)) #showing the result 
