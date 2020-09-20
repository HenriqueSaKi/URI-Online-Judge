#URI Online Judge - Exercise Number 1020

Idade = int(input())

anos = Idade/365
meses = (Idade%365)/30
dias = ((Idade%365)%30)


print ("%i" %(anos), "ano(s)")
print ("%i" %(meses), "mes(es)")
print ("%i" %(dias), "dia(s)")
