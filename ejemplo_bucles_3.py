import math
print("Programa de calculo de raiz cuadrada.")

numero=int(input("Introduce un número por favor: "))
intentos=0
solucion=0

while numero<0:
	intentos=intentos+1
	print("No se puede hallar la raiz de un número negativo.")
	
	if intentos==2:
		print("número de intentos superado...")
		break;
	else:
		numero=int(input("Introduce un número por favor: "))
	

if intentos<2:
	solucion=math.sqrt(numero)

print(solucion)
