def evaluacion(nota):
	valoracion="aprobado"
	if nota<5: 
		valoracion="suspenso"
	return valoracion

#nota = input()
#print("resultado")
#print(evaluacion(int(nota)))

def mayorDeEdad(edad):
	edadUsuario=""
	if edad>=18:
		edadUsuario="Es mayor de edad"
	elif 0<edad<18:
		edadUsuario="NO es mayor de edad"
	else:
		edadUsuario="Error al introducir la edad"

	return edadUsuario

edad_usuario=int(input("dime tu edad: "))
print(mayorDeEdad(edad_usuario))