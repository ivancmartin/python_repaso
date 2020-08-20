class Coche():
	def desplazamiento(self):
		print("Me desplazo a 4 ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo a 2 ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo a 6 ruedas")

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Moto()
desplazamientoVehiculo(miVehiculo)
