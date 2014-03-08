#!/bin/sh
import numpy as np
import scipy as sp
from pylab import *
import math
import struct
import funcionFitness
import funcionRuleta


#Esta es la array que contienen el problema principal, la idea es encontrar la recta que mejor se acerque a estos puntos, a todos!!
dataArray = ((109,1),(149,2),(149,3),(191,5),(213,7),(224,10))


def binary(num):
    return 

def f(b1,b2,x):
	# Aqui se calculan los valores acotados al random para regresar la poblacion inicial
	return b1*(1-exp((-b2)*x))

def generaPoblacionInicial():
	arrayB1 = np.random.uniform(105, 225, size=100)
	#print "arrayB1", arrayB1
	arrayB2 = np.random.uniform(105, 225, size=100)
	#print "arrayB2", arrayB2
	return zip(arrayB1, arrayB2)

def convierteABinario(poblacion):
	componenteX = []
	componenteY = []

	for x in poblacion:
		value = []
		stringFromFloat = str(x[0])
		stringFromFloat = stringFromFloat.split(".")
		stringFromFloatOnL = stringFromFloat[0]
		stringFromFloatOnR = stringFromFloat[1]
		value.append(bin(int(stringFromFloatOnL)))
		value.append(bin(int(stringFromFloatOnR)))
		componenteX.append(value)
		value = []
		stringFromFloat = str(x[1])
		stringFromFloat = stringFromFloat.split(".")
		stringFromFloatOnL = stringFromFloat[0]
		stringFromFloatOnR = stringFromFloat[1]
		value.append(bin(int(stringFromFloatOnL)))
		value.append(bin(int(stringFromFloatOnR)))
		componenteY.append(value)
		
		# componenteX.append(binary(x[0]))
		# componenteY.append(binary(x[1]))
		# print componenteX, componenteY
	#print componenteX, componenteY
	return zip(componenteX, componenteY)

def calculaMinimosCuadrados(poblacion):
	
	distancias = []
	
	#print "Ciclo For---------------------------------------------------"
	for item in poblacion:
		distCuadratica = 0
		for x in dataArray:
			elementosASumar = []
			#print "(b1, b2) , x", item, x[1]
			algo= (-1)*item[1]*x[1]
			#print "-b2*x", algo
			algo2 = math.exp(algo)
			#print "exp(-b2*x)", algo2
			algo3 = 1-algo2
			#print "1-exp(-b2*x)", algo3
			algo4 = algo3*item[0]
			#print "Ecuacion evaluada ", algo4
			elementosASumar.append(math.pow(x[0]-algo4,2))
			#print "-----------------------------------------------------------"
		#print "Elementos del Array a sumar y-yi",x[0], elementosASumar	
		for j in elementosASumar:
			distCuadratica = distCuadratica + j
			#print distCuadratica
		distancias.append(distCuadratica)
		distCuadratica=0
	return distancias

def regresaBinariosEnTuplas(distanciasEnBinario):
	arrayDeBinarios = []
	#print distanciasEnBinario
	for x in distanciasEnBinario:
		tuplaAuxiliar = []
		#print x
		tuplaAuxiliar.append(x[:-16])
		tuplaAuxiliar.append(x[16:])
		arrayDeBinarios.append(tuplaAuxiliar)
		#print tuplaAuxiliar
	return #arrayDeBinarios

 # La poblacion inicial se genera a partir de elementos aleatorios de entre los valores 
 # aproximados al minimo y al maximo valor de y de entre todos
 # los valores de y en la tabla del problema
poblacionInicial = generaPoblacionInicial()
#print poblacionInicial

# El metodo soguiente recibe la pobalcion inicial para posteriormente regresar las distancias  de cada uno de los
# elementos de la poblacion inicial con respecto de los puntos del problema
distPorElementos = calculaMinimosCuadrados(poblacionInicial)
#print distPorElementos

dummyArreglo = funcionRuleta.funcRuleta(distPorElementos, poblacionInicial)
print dummyArreglo

# # Este metodo convierte los elementos en su representacion  binaria y los regresa a una matriz 
# elementosEnBinario = convierteABinario(poblacionInicial)
# #print elementosEnBinario
# # for x in elementosEnBinario:
# # 	print x[0][0], x[0][1], x[1][0], x[1][1]

# elementosOrdenadosPorDistancias = funcionFitness.funcionDeFitness(poblacionInicial, distPorElementos)
# print elementosOrdenadosPorDistancias
# elementosOrdenadosEnBinario = convierteABinario(elementosOrdenadosPorDistancias)
# print elementosOrdenadosEnBinario


# elementosOrdenadosEnBinario = calculaMinimosCuadrados(elementosOrdenadosPorDistancias)
# elementosOrdenadosEnBinario = convierteABinario(elementosOrdenadosEnBinario)

# Este metodo ordena en una matriz de tuplas los elementos partidos por la mitad de su representacion bianria
#nuevosElementos = regresaBinariosEnTuplas(elementosEnBinario)
#print nuevosElementos

# for x in nuevosElementos:
# 	if nuevosElementos.next is None:
# 		print x, nuevosElementos.next

