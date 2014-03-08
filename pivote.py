import random
import numpy as np

#regresa la posicion en donde debe estar el pivote
def regresapivote(padre, madre):
	
	pad = padre[1]
	mad = madre[1]
	
	#elimina la cadena 0b del inicio de las cadenas binarias
	#pad = pad[2:len(padre[1])]
	#mad = mad[2:len(madre[1])]
	
	pivotes = []
	
	tamanoCromosomaEntera=8
	#tamano minimo entre los dos cromosomas a cruzar(parte fraccionaria)
	tamanoCromosomaFracc = 0
	if len(pad)<len(mad):
		tamanoCromosomaFracc= len(pad)
	else:
		tamanoCromosomaFracc= len(mad)
	
	#genera el pivote en la parte entera
	rand = random.random()
	
	probAcumuladas = probabilidadesAcumuladasPivotes(8)
	
	for i in range(len(probAcumuladas)-1):
		
		if (probAcumuladas[i]<rand) & (rand < probAcumuladas[i+1]):
			pivotes.append(8-i)
			break
	
	#genera el pivote en la parte fraccionaria
	rand = random.random()
	
	probAcumuladas = probabilidadesAcumuladasPivotes(tamanoCromosomaFracc)
	
	for i in range(len(probAcumuladas)-1):
		
		if (probAcumuladas[i]<rand) & (rand < probAcumuladas[i+1]):
			pivotes.append(tamanoCromosomaFracc-i)
			break
		
	return pivotes



def probabilidadesAcumuladasPivotes(tamanoCromosoma):#genera las probabilidades de escoger cierta posicion para el pivote
	#primero asigna una aptitud a los valores posibles del pivote
	probabilidadesAcumuladas = []
	probabilidades = []
	aptitudes = []
	for i in range(tamanoCromosoma):
		aptitudes.append(i+1)
	
	#suma todas las aptitudes
	sumaAptitudes = 0
	for i in aptitudes:
		sumaAptitudes = sumaAptitudes + i
	
	for i in aptitudes:
		probabilidades.append(i/float(sumaAptitudes))
		
	for i in range(len(probabilidades)):
		suma = 0
		for ind in range(i):
			suma = suma + probabilidades[ind]
		probabilidadesAcumuladas.append(suma)
	
	probabilidadesAcumuladas.append(1)
	
	return  probabilidadesAcumuladas





#pruebas
padre = []
padre.append("00000000")
padre.append("111111111111")

madre = []
madre.append("00000000")
madre.append("111111111111")

print regresapivote(padre,madre)



