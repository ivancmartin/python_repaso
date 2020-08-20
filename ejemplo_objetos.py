class Coche():

	def __init__(self):
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enMarcha=False

	def arrancar(self,arrancamos):
		self.__enMarcha=arrancamos

		if self.__enMarcha:
			chequeo=self.__chequeo_interno()


		if self.__enMarcha and chequeo:
			return "el Coche está en marcha"
		
		elif self.__enMarcha and chequeo==False:
			return "Algo ha ido mal en el chequeo"

		else:
			return "el Coche está parado"


	def acelerar(self):
		return True


	def estado(self):
		print("el coche tiene: ", self.__ruedas ," ruedas. un ancho de: ", 
			self.__anchoChasis, " y un largo de: ", self.__largoChasis)


	def __chequeo_interno(self):
		print("realizando chequeo interno...")

		self.gasolina = "OK"
		self.aceite = "OK"
		self.puertas = "Cerradas"

		if self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "Cerradas":
			return True
		else:
			return False


miCoche=Coche()

miCoche.estado() 
print(miCoche.arrancar(True)) 

print("---------------")
miCoche2=Coche()
miCoche2.estado() 
print(miCoche2.arrancar(False))

