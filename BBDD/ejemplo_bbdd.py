import sqlite3

miConexion=sqlite3.connect("PrimeraBase")
miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balón',15,'Deportes')")
miCursor.execute("DROP TABLE PRODUCTOS")

variosProductos=[
	("Camiseta",10,"Deportes"),
	("Jarrón",90,"Cerámica"),
	("Camión",20,"Jugetería")
]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)


try:
	miCursor.execute('''
		CREATE TABLE PRODUCTOS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NOMBRE_ARTICULO VARCHAR(50), 
		PRECIO INTEGER, 
		SECCION VARCHAR(20))
	''')

except Exception as e:
	print(e)

try:
	variosProductos2=[
		("Pelota",20,"Jugetería"),
		("Pantalón",15,"Confección"),
		("Destornillador",25,"Ferretería"),
		("Jarrón",20,"Cerámica")
	]

	miCursor.executemany("INSERT INTO PRODUCTOS VALUES(null,?,?,?)",variosProductos2)

except Exception as e:
	print(e)


miCursor.execute("SELECT * FROM PRODUCTOS")
print

miConexion.commit()



miConexion.close()