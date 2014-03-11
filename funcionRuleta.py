#!/bin/sh
import numpy as np
import scipy as sp

def funcRuleta(distanciasTotales,poblacioninicial):
	aptitudTotal = 0
	probabilidades = []
	arregloParticiones = []

	#print poblacioninicial

	for x in distanciasTotales:
		aptitudTotal = aptitudTotal + x

	for y in distanciasTotales:
		probabilidades.append(y/aptitudTotal)

	sumaParticion = 0
	for item in probabilidades:
		sumaParticion = sumaParticion + item
		arregloParticiones.append(sumaParticion)


	#print probabilidades
	

	arregloDeElegidos = []
	#print arregloParticiones

	for item in range(0,2):
		r = np.random.uniform(0,1)
		#print r
		elElegido = 0
		for x in zip(arregloParticiones, poblacioninicial):
		 	if(r<x[0]):
		 		elElegido = x[1]
		 		arregloDeElegidos.append(elElegido)
		 		poblacioninicial.remove(elElegido)
		 		arregloParticiones.remove(x[0])
		 		#print x[0]
		 		break


	#print poblacioninicial
	#print arregloParticiones
	#print elElegido
	#print arregloParticiones
	#print arregloDeElegidos

	#print probabilidades
	

	

	return arregloDeElegidos
