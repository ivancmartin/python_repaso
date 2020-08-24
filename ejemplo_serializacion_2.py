import pickle
class Vehiculos():
	
	def __init__(self,marca,modelo):
		self.modelo=modelo
		self.marca=marca
		self.enMarcha=False
		self.acelera=False
		self.frena=False 

	def arrancar(self):
		self.enMarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frenar=True

	def estado(self):
		print("Marca; ", self.marca, 
			  "\nModelo: ", self.modelo,
			  "\nEn marcha: ", self.enMarcha,
			  "\nAcelerando: ", self.acelera,
			  "\nFrenando: ", self.frena)

cohe1=Vehiculos("Mazda","MX5")
cohe2=Vehiculos("Seat","Leon")
cohe3=Vehiculos("Renault","Megane")

coches=[cohe1,cohe2,cohe3]
fichero=open("los_coches","wb")
pickle.dump(coches,fichero)
fichero.close()

del(fichero)

