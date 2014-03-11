import random
 
def muta(poblacion):
    print poblacion
    probabilidadMutacion = .1
    for i in range(len(poblacion)):
        for e in range(len(poblacion[i])):
            for a in range(len(poblacion[i][e])):
                for ind in range(len(poblacion[i][e][a])):

                    if(ind==0 or ind ==1):
                        continue
                    rand = random.random()
                    if (rand<probabilidadMutacion):
                        if (poblacion[i][e][a][ind]=="0"):
                            poblacion[i][e][a] = poblacion[i][e][a][:ind]+"1"+poblacion[i][e][a][ind+1:]
                        else:
                            poblacion[i][e][a] = poblacion[i][e][a][:ind]+"0"+poblacion[i][e][a][ind+1:]

    # for i in poblacion:
    #     print i[0][0], i[0][1]
    #     #print i[1][0], i[1][1]

    #     for x in i[0][0][2:]:
    #         rand = random.random()
    #         if (rand < probabilidadMutacion):
    #             if (x == "0"):
    #                 x = "1"
    #                 print "Cambio 0 por 1"
    #             else:
    #                 x = "0"
    #                 print "Cambio 1 por 0"
    #     print i
    print poblacion