# Projet 1 page 25
# Version 3.2.1
# Version en cours de documentation

import time
from numbers_dict import *

#classe des couleurs
class basics_colors:
    OK = '\033[92m' #VERT -> réponse 
    FAIL = '\033[91m' #ROUGE -> code d'erreur
    RESET = '\033[0m' #GRIS -> remet les couleurs à 0

def error_message(args): # envoyé avec args, envoie un message d'erreur
    print(basics_colors.FAIL, errors_dict[args] ,basics_colors.RESET)
    time.sleep(1)
    requestType()
    
#exercice 1 
def decimale_binaire(n): # envoyé grace à requestType(), renvoie la fonction de demande de calcul pour la base 2
    req_value_1 = input("donnez un chiffre en base 10 \n >>>")

    if (req_value_1.isdigit()):
        n = int(req_value_1)
        if n == 0 or n == 1: # valeurs par defaut
            print(basics_colors.OK, n, " vaut ", n," en toutes les bases ", basics_colors.RESET)
        if n < 0: # erreur
            args = 2
            error_message(args)
        req_binary(n)
    else: # erreur
        args = 4
        error_message(args)

def req_binary(n): # envoyé par requestType(), prend en fonction le nombre n demande, renvoie la fonction calculatoire du calcul binaire
    vInit = n
    binary_list = []
    while n != 0:
        varList = n % 2
        binary_list.insert(0, varList)
        n = n // 2

    if n == 0:
        resList = ' ,'.join(map(str,binary_list))
        resListTotal = ''.join(map(str,binary_list)) 
        print(basics_colors.OK, vInit, " en base 10 équivaut à ", resList, " ( ", resListTotal, " ) en base 2", basics_colors.RESET)
        time.sleep(1.5)
        requestType()
    #end decimale_binaire

# exercice 2
def decimale_hexadecimale(n): # envoyé grace à requestType() ou req_binary(), renvoie la fonction de demande de calcul pour la base 16
    n = 0
    req_value_1 = input("donnez un chiffre en base 10 \n >>>")

    if ( req_value_1.isdigit()):
        n = int(req_value_1)

        if n == 0 or n == 1: # valeurs par défaut
            print(basics_colors.OK, n, " vaut ", n," en toutes les bases ", basics_colors.RESET)
            time.sleep(1)
            requestType()

        if n < 0: # erreur
            args = 2
            error_message(args)
        reqBase = 16
        req_hexa(n, reqBase) # renvoie à la partie calculatoire vers la base 16 avec n et la base demandée(obligatoirement 16)

    else: # erreur
        args = 4
        error_message(args)
    
def req_hexa(n, reqBase): # envoyé par decimale_hexadecimal(), prend en compte n et la base 16, calcule le résultat
    
    varListStr = 0
    vInit = n
    binary_list = []
    while n != 0:
        varList = n % reqBase
        n = n // reqBase

        if varList > 9: # si c'est un chiffre (0 -> 9 )
            binary_list.insert(0, numbers_dict[varList])
        if varList <= 9: # si supérieur à 9 renvoie les lettres
            binary_list.insert(0, varList)
            
        if n == 0:
            resList = ' ,'.join(map(str,binary_list)) # faire une liste visible
            resListTotal = ''.join(map(str,binary_list)) # faire une liste visible
            print(basics_colors.OK, vInit, " en base 10 équivaut à ", resList, " ( ", resListTotal, " ) en base ", reqBase, basics_colors.RESET)
            time.sleep(3)
            requestType()
    # end decimale_hexadecimale
    
# exercice 3
def base_request(n):
    n = 0
    req_value_1 = input("donnez un chiffre en base 10 \n >>> ")

    if ( req_value_1.isdigit()):
        vInit = int(req_value_1)
        n = int(req_value_1)

        if n < 0: # erreur
            args = 2
            error_message(args)
        if n == 0 or n == 1: # valeurs par défaut
            print(basics_colors.OK, n, " vaut ", n," en toutes les bases ", basics_colors.RESET)
            time.sleep(1)
            requestType()

        req_value_2 = input("donnez la base en laquelle vous voulez convertir  \n >>>")

        if ( req_value_2.isdigit()):
            reqBase = int(req_value_2)

            if reqBase <= 1: # erreur
                args = 3
                error_message(args)
            if reqBase > 36: # erreur
                args = 5
                error_message(args)

            binary_list = []

            if reqBase == 2: #renvoie vers l'exercice de base 2
                req_binary(n)
                requestType()
            else:
                req_hexa(n, reqBase) #renvoie vers l'exercice de base 16
                requestType()

        else:
            args = 4
            error_message(args)
    else:
        args = 4
        error_message(args)

# demande ce que l'user veut faire 
def requestType():
    request = input("que voulez vous faire ? \n '1' -> conersion décimale vers binaire \n '2' -> conversion décimale vers hexadécimale \n '3' -> conversion décimale vers base demandée \n >>>")
    
    if ( request.isdigit()):
        n = int(request)
        if n > 3 or n <= 0:
            args = 1
            error_message(args)
        if n == 1: 
            decimale_binaire(n) # -> Exercice 1 -> partie du calcul
            return()
        if n == 2:
            decimale_hexadecimale(n) # -> Exercice 2 -> partie du calcul
            return()
        if n == 3:
            base_request(n) # -> Exercice 3 -> partie de demande puis de calcul
            return()
    else:
        args = 4
        error_message(args)

#debut du code
requestType()
