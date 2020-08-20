nombre="Pildoras informaticas"
print(len(nombre))
contador=0

for i in nombre:
	if i==" ":
		continue
	contador+=1

print(contador)

for letra in "Python":
	if letra=="h":
		continue
	print(letra)


email="ivan@mail.es"
arroba=False

for i in email:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False

print(arroba)