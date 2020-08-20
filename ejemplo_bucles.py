for i in ["hola","que","tal"]:
	print(i,end=" ")

print(" ",end="\n")

cont=0
direccEmail="ivan@ivan.es"

for i in direccEmail:
	if (i == "@" or i=="."):
		cont=cont+1


print(cont)
if cont == 2:
	print("email correcto")
else:
	print("email NO correcto")


for i in range(1,20,2): #valor inicial, valor final, saltos(de uno en uno, de dos en dos....)
	print(f"valor de la variable {i}")

valido=False
email=input("Introduce tu email: ")
for i in range(len(email)):
	if email[i] == "@":
		valido=True

if valido:
	print("correcto")
else:
	print("incorrecto")

		