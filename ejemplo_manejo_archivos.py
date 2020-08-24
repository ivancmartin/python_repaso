from io import open

archivo_texto=open("archivo.txt","w")
frase="Estupendo día para estudiar python \nel miércoles"
archivo_texto.write(frase)
archivo_texto.close()

archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)

archivo_texto=open("archivo.txt","r")
texto=archivo_texto.readlines()
archivo_texto.close()
print(texto[1])

archivo_texto=open("archivo.txt","a")
texto=archivo_texto.write("\nSiempre es una buena ocasion para estudiar python")
archivo_texto.close()

archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)

print("----------- seek ------------")

archivo_texto=open("archivo.txt","r")
archivo_texto.seek(10)
texto=archivo_texto.read()
print(texto)
archivo_texto.close()

print("------------- read hasta -----------")
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read(10)
print(texto)
texto=archivo_texto.read()
print(texto)
archivo_texto.close()

print("------------- ejemplo seek y len -----------")
archivo_texto=open("archivo.txt","r")
archivo_texto.seek(len(archivo_texto.read())/2)
texto=archivo_texto.read()
print(texto)
archivo_texto.close()
