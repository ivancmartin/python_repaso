miTupla=("Juan",13,1,1995,"Juan")
miLista=list(miTupla) #convertir una tupla en una lista

print(miTupla[:2])
print(miLista)

print("Juan" in miTupla) #compprobar que el elemento existe
print(miTupla.count("Juan")) #compprobar total de veces que aparece un elemento
print(len(miTupla)) 

miLista2=["otro","ejemeplo",2]
miTupla2=tuple(miLista2)

print(miTupla2)
print(miLista2)

miTuplaUnitaria=("Juan",) #tupla unitaria
print(len(miTuplaUnitaria)) 

miTuplaSinParentesis=13,1,1995,"Juan" #empaquetado de tupla
print(miTuplaSinParentesis) 

miTuplaADesempaquetar=13,1,1995,"Juan" #desempaquetado de tupla
dia,mes,ano,nombre = miTuplaADesempaquetar
print(dia)
print(mes)
print(nombre)




