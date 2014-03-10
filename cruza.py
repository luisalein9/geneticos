
import random

def randomT(poblacion):
	print 'la tupla es ', poblacion
	x=random.randint(0, 8)

	return x

def long8(cadena):

	if len(cadena) < 10:

		caCero=""
		ceros=10-len(cadena)
		for i in range(ceros):
			caCero=caCero+"0"
		cFinal=cadena[0:2]+ caCero +cadena[2:10]
		cadena=cFinal

	return cadena

def cruzaEnt(entero1, entero2, posiciones):
	pos=10-int(posiciones)
	if pos > 0 & pos < 8 :
		p1entero1=entero1[0:pos]
		p2entero1=entero1[pos:10]
		p1entero2=entero2[0:pos]
		p2entero2=entero2[pos:10]

		entero1=p1entero1+p2entero2+""
		entero2=p1entero2+p2entero1+""

	lista = [entero1,entero2]

	return lista

def cruzaDec(decimal1, decimal2,posiciones):
	pos=int(posiciones)
	pos1=len(decimal1)-int(posiciones)
	pos2=len(decimal2)-int(posiciones)

	if pos > 0 & pos < pos1 & pos < pos2 :
		p1decimal1=decimal1[0:pos1]
		p2decimal1=decimal1[pos1:len(decimal1)]
		p1decimal2=decimal2[0:pos2]
		p2decimal2=decimal2[pos2:len(decimal2)]

		decimal1=p1decimal1+p2decimal2+""
		decimal2=p1decimal2+p2decimal1+""

	lista = [decimal1,decimal2]

	return lista

def cruzaPob(poblaciones):

	x1=""
	x2=""
	y1=""
	y2=""
	listaFin=[]
	listaFin1=[]
	listaFin2=[]
	tuplaF=[]
	#Tomo tupla por tupla los elementos de la poblacion
	for poblacion in poblaciones:
		#Defino el numero de posiciones que cruzare
		posicion=randomT(poblacion);
		print posicion

		for (x, y) in poblacion:

			if x1 =="" :
				x1=long8(x)
				y1=y


			else :
				x2=long8(x)
				y2=y

				lista1=cruzaEnt(x1, x2, posicion)
				lista2=cruzaDec(y1, y2, posicion)

				l1T=[lista1[0],lista2[0]]
				l2T=[lista1[1],lista2[1]]

				listaFin1.append(l1T)
				listaFin2.append(l2T)
				x1=""
				x2=""
				y1=""
				y2=""


	listaFin=zip(listaFin1, listaFin2)


	print "La lista final es => ", listaFin
	print "La lista inicial es => ", poblaciones

	return listaFin