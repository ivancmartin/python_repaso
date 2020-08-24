import pickle
from ejemplo_objetos_herencia import *
print("-- recoger datos coches --")

ficheroApertura=open("los_coches","rb")
misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for i in misCoches:
	print(i.estado(),"\n")
