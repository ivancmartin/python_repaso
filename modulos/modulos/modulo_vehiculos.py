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

class Moto(Vehiculos):
	hcaballito=""

	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print("Marca; ", self.marca, 
			  "\nModelo: ", self.modelo,
			  "\nEn marcha: ", self.enMarcha,
			  "\nAcelerando: ", self.acelera,
			  "\nFrenando: ", self.frena,
			  "\n",self.hcaballito)

class Furgoneta(Vehiculos):
	
	def carga(self,cargar):
		self.cargado=cargar
		if self.cargado:
			return "la Furgoneta esta cargada"
		else:
			return "la Furgoneta NO esta cargada"

class VElectricos(Vehiculos):

	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True

class BicicletaElectrica(VElectricos,Vehiculos):
	pass
