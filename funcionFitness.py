def funcionDeFitness(poblacion, distanciasPorElemento):
	
	copiaPoblacion = poblacion
	copiaDistancias = distanciasPorElemento

	#print poblacion
	#print copiaDistancias
	diccionario = {}

	for (x1, x2) in zip(copiaDistancias, copiaPoblacion):
		diccionario[x1] = x2

	#print diccionario

	copiaDistancias = sorted(copiaDistancias)

	#print copiaDistancias

	elementoOrdenados =[]
	for x in copiaDistancias:
		elementoOrdenados.append(diccionario[x])

	return elementoOrdenados