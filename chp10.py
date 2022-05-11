def sac_a_dos(liste, masse_max):
    encours = []
    for i in range(len(liste)):
        encours = liste[i][1]//liste[i][2]
    totalactual = 0 
    sacadostot = []
    n = 0 
    while totalactual + liste[n][3] < masse_max:
        sacadostot.append(n)

    return sacadostot

def rendu_de_monnaie(somme_restante, system):
    somme = somme_restante
    rendu = []
    i = 0
    while somme != 0:
        while system[i] > somme:
            i += 1
    rendu[i] = somme / system[i]
    somme = somme % system[i]
    return rendu

def evolue_lettre(lettre1, lettre2):
    l1 = ord(lettre1)
    l2 = ord(lettre2) 
    if l2 > l1:
        l3=l2-l1
    else:
        l3= 90 - l1 + abs(64 - l2)
    if l3 % 13 == 0:
        l3 = l3 // 13
    return l3

def evolue(mot1, mot2):
  jours = 0
  print(mot1)
  print(mot2)
  for i in str(mot1):
    for j in str(mot2):
      jours += evolue_lettre(i,j)
  return jours

#revoir mot et lettre 

# pas compris acti 5 

def d_hamming(nb1,nb2):
    difference = 0
    for i in nb1:
        for j in nb2:
            if i != j:
                difference += 1
    return difference


def dichotomie(list, val):
    value = val
    init = 0
    obj = len(list)
    trouve = False
    while trouve == False and init < obj:
        k= (init + obj) / 2
        if list[k] == value:
            trouve = True
        else:
            if list[k]>value:
                obj = k
            else:
                init = k
    return k
