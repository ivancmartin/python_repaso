def numPares(limit):
	num=1
	while num<limit:
		yield num*2
		num=num+1

devuelvePar=numPares(10) 

#cuidado al recorer el for antes de usar la funcion iteradora next, no furula
#for i in devuelvePar:
#	print(i)

#print(next(devuelvePar))


#el * significa que no se save cuantos de argumentos va a recibir y 
#los recibirá en forma de TUPLA
def devuelveCitys(*ciudades):
	for elemento in ciudades:
		#for subElemento in elemento:
			#yield subElemento
			
		yield from elemento

ciudadesDevueltas=devuelveCitys("Madrid","Barcelona","Bilbao","valencia")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))


