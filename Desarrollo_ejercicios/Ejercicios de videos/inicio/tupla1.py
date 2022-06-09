tupla1=("Juan",13,1,1995,1,1)
listatupla1=list(tupla1)
tupladelista=tuple(listatupla1)
tupla2=tupla1+tupla1
listatupla2=list(tupla2)
print(listatupla1)
print(tupladelista)
print(listatupla2)
print("Hay " + str(tupladelista.count(1)) + " unos en la tupla")

