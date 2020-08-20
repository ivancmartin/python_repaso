def evaluaEdad(edad):
	
	if edad<0:
		raise TypeError("la edad no puede ser menor que 0")

	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	elif edad<100:
		return "Cuidate"

print(evaluaEdad(50))

