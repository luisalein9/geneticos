import random
 
def muta(poblacion):
    print poblacion
    probabilidadMutacion = 0.4
    for i in poblacion:
        for e in i:
            for a in e:
                for ind in range(len(a)):
                    rand = random.random()
                    if (rand<probabilidadMutacion):
                        if (a[ind]=="0"):
                            a = a[:ind]+"1"+a[ind+1:]
                        else:
                            a = a[:ind]+"0"+a[ind+1:]

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