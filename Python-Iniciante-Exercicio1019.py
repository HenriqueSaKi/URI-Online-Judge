#URI Online Judge - Exercise Number 1019

N = int(input())

seconds = N%60
minutes = (N/60)%60 
hours = N/3600 
print("%i:%i:%i" %(hours, minutes, seconds))
