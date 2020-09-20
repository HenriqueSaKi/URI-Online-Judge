#URI Online Judge - Exercise Number 1009

name = input() #employee name
n2 = float(input()) #salary
n3 = float(input()) #sale value

n3 = n3*0.15 #the condittion of payment
total = n3+n2 #sum of it's salary and a part of sale
print("TOTAL = R$ %.2f" %(total)) #show the result
