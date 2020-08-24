import pickle
listaNombre=["Pedro","Ana","María","Isabel"]

ficheroBinario=open("lista_nombres","wb")

pickle.dump(listaNombre,ficheroBinario)

ficheroBinario.close()

del(ficheroBinario)

print("--- cargar fichero binario ------")

fichero=open("lista_nombres","rb")
lista_nombres=pickle.load(fichero)
print(lista_nombres)

