print("Introduce los siguientes datos")
nombre=input("Dime tu nombre: ")
direccion=input("Dime tu direccion: ")
tlfno=input("Dime tu teléfono: ")


def guardarDatos(nombre,direccion,tlfno):
	datusUsu=[nombre,direccion,tlfno]
	return datusUsu

datos=guardarDatos(nombre,direccion,tlfno)

print('los datos son: nombre: '+ datos[0] + ';  direccion' + datos[1] + '; telefono: ' + datos[2])
