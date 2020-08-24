nombre=input("Introduce un nombre de usuario: ")
print(f"El nombre es: {nombre.upper()}")
print(f"El nombre es: {nombre.lower()}")
print(f"El nombre es: {nombre.capitalize()}")
print(f"El nombre es un numero?: {nombre.isdigit()}") 

edad=input("Introduce una edad: ")
while edad.isdigit()==False:
	
	edad=input("Error! Introduce de nuevo una edad: ")


if int(edad)>=18:
	print("puedes pasar")
else:
	print("NO puedes pasar")

