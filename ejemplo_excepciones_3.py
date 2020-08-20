import math

def calcularRaiz(num):
	if num<0:
		raise ValueError("El numero no puede ser negativo")
	else:
		return math.sqrt(num)

num1=(int(input("Intro un num: ")))

try:
	print(calcularRaiz(num1))
except ValueError as ErrorNumNegativo:
	print(ErrorNumNegativo)

	

print("Programa terminado")