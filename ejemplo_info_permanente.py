import pickle

class Persona:
	def __init__(self,nombre,genero,edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print(f"Se a creado una persona con el nombre: {self.nombre} ")

	def __str__(self):
		return "{} {} {}".format(self.nombre,self.genero,self.edad)


class listaPersonas:
	personas=[]

	def __init__(self):
		listaDePersonas=open("fichero_externo", "ab+")
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargarno {} personas del fichero".format(len(self.personas)))
			
		except:
			print("El fichero está vacío")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)


	def agregarPersona(self,persona):
		self.personas.append(persona)

	def mostrarPersonas(self):
		for i in self.personas:
			print(i)

	def guardarPersonasEnFichero(self):
		listaDePersonas=open("fichero_externo", "wb")
		pickle.dump(self.personas,listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("La informacion del fichero externo es la siguiente: ")
		for i in self.personas:
			print(i)

miLista=listaPersonas()

miPersona=Persona("Iván","Masculino",26)
miPersona2=Persona("Rubén","Masculino",26)
miPersona3=Persona("Beatriz","Femenino",26)

miLista.agregarPersona(miPersona)
miLista.agregarPersona(miPersona2)
miLista.agregarPersona(miPersona3)

miLista.mostrarPersonas()
miLista.guardarPersonasEnFichero()
miLista.agregarPersona(miPersona3)
miLista.guardarPersonasEnFichero()

print("-------------------")
miLista.mostrarInfoFicheroExterno()