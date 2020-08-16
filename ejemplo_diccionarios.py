miDiccionario={"Alemania":"Berlin","Francia":"París","Reino unido":"Londres","España":"Madrid"}
print(miDiccionario["España"])

miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

miDiccionario["Italia"]="Roma" #se sobreescriben valores
print(miDiccionario)

del miDiccionario["Reino unido"] #borrar valores
print(miDiccionario)

miDiccionario2 = {"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}
print(miDiccionario2)

miTupla=["España","Francia","Reino unido","Alemania"]
miDiccionario3={miTupla[0]:"Madrid",miTupla[1]:"París",miTupla[2]:"Londres",miTupla[3]:"Berlin"}
print(miDiccionario3["Francia"])

miDiccionario4={23:"Jordan","nombre":"Michel","equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario4["anillos"]["temporadas"][0])
print(miDiccionario4.keys())
print(miDiccionario4.values())
print(len(miDiccionario4))

