miLista=["maría",False,5,"Antonio"]

#miLista.append("Sandra") #añadir al final

#miLista.insert(2,"Sandra") #añadir en el indice indicado

miLista.extend(["Sandra","Ana","Lucia"]) #añadir un conjunto de elementos

#print(miLista.index("Pepes"))

print("Pepe" in miLista) #comprobar si exsite en la lista

miLista.pop() #eliminar el ultimo elemento 

miLista.remove("maría") #elimina la 1º coincidencia


print(miLista[:])

miLista2=["otros","valores"]*2 # *n -> se repite la lista nveces

miLista3=miLista+miLista2 #'concatenar' arrays

print(miLista3[:])

