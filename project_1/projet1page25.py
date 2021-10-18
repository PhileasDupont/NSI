# Projet 1 page 25
Version = 'V4.2.1'
# Version en cours de documentation

import time
from numbers_dict import *
import webbrowser

#classe des couleurs
class color:
    OK = '\033[92m' #VERT -> réponse 
    FAIL = '\033[91m' #ROUGE -> code d'erreur
    RESET = '\033[0m' #GRIS -> remet les couleurs à 0

def error_message(args): # envoyé avec args, envoie un message d'erreur
    print(color.FAIL, errors_dict[args] ,color.RESET)
    time.sleep(1)
    requestType()

def verif(request):
    if request == 'r' or request == 'restart':
        print(color.OK, ' retour au début ...', color.RESET)
        time.sleep(0.5)
        requestType()
    if request == 'help' or request == 'h':
        print(color.OK,"redirection sur le GitHub ...", color.RESET)
        webbrowser.open('https://github.com/PhileasDupont/NSI/blob/main/project_1/')
        time.sleep(2)
        requestType()
    if request == 'q' or request == 'quit':
        print(color.FAIL, "Merci d'avoir participé !", color.RESET)
        print(color.OK, "Created by ©PhileasDupont", color.RESET)
        print(color.OK, Version, color.RESET)

        time.sleep(1)
        exit()

def binaire_hexa(n, reqBase): # envoyé grace à requestType()
    request = input("donnez un chiffre en base 10 \n >>>")
    verif(request)
    if ( request.isdigit()):
        n = int(request)
        if n == 0 or n == 1: # valeurs par défaut
            print(color.OK, n, " vaut ", n," en toutes les bases ", color.RESET)
            time.sleep(1)
            requestType()
        if n < 0: # erreur
            args = 2
            error_message(args)
        req(n, reqBase)
    else:
        args = 4
        error_message(args)
    
def req(n, reqBase): # envoyé par decimale_hexadecimal(), prend en compte n et la base 16, calcule le résultat    
    vInit = n
    binary_list = []
    while n != 0:
        varList = n % reqBase
        n = n // reqBase

        binary_list.insert(0, alpha[varList])

        if n == 0:
            resList = ' ,'.join(map(str,binary_list)) # faire une liste visible
            resListTotal = ''.join(map(str,binary_list)) # faire une liste visible
            print(color.OK, vInit, " en base 10 équivaut à ", resList, " ( ", resListTotal, " ) en base ", reqBase, color.RESET)
            time.sleep(3)
            requestType()
    # end decimale_hexadecimale   
# exercice 3
def base_request(n):
    n = 0
    request = input("donnez un chiffre en base 10 \n >>> ")
    verif(request)
    if ( request.isdigit()):
        vInit = int(request)
        n = int(request)

        if n < 0: # erreur
            args = 2
            error_message(args)
        if n == 0 or n == 1: # valeurs par défaut
            print(color.OK, n, " vaut ", n," en toutes les bases ", color.RESET)
            time.sleep(1)
            requestType()

        request = input("donnez la base en laquelle vous voulez convertir  \n >>>")
        verif(request)
        if ( request.isdigit()):
            reqBase = int(request)
            if reqBase <= 1: # erreur
                args = 3
                error_message(args)
            if reqBase > 62:
                args = 5
                error_message(args)
            binary_list = []
            req(n, reqBase) #renvoie vers l'exercice de base 16

        else:
            args = 4
            error_message(args)
    else:
        args = 4
        error_message(args)

# demande ce que l'user veut faire 
def requestType():
    print(color.OK, "debut du programme ...", color.RESET)
    print(color.OK, Version, color.RESET)
    time.sleep(1)
    print("que voulez vous faire ? \n '1' -> conersion décimale vers binaire \n '2' -> conversion décimale vers hexadécimale \n '3' -> conversion décimale vers base demandée \n A n'importe quel moment tapez", color.FAIL, ' r ', color.RESET, "pour", color.FAIL, " RECOMMENCER ", color.RESET, ", tapez", color.FAIL, " h ", color.RESET, "pour être", color.FAIL, " redirigé vers la page d'aide ", color.RESET, "ou tapez", color.FAIL, " q ", color.RESET, "pour", color.FAIL, " QUITTER", color.RESET)
    request = input(">>>")
    verif(request)
    if ( request.isdigit()):
        n = int(request)
        if n > 3 or n <= 0:
            args = 1
            error_message(args)
        if n == 1: 
            reqBase = 2
            binaire_hexa(n, reqBase)
            return()
        if n == 2:
            reqBase = 16
            binaire_hexa(n, reqBase)
            return()
        if n == 3:
            reqBase = 0
            base_request(n) # -> Exercice 3 -> partie de demande puis de calcul
            return()
    else:
        args = 4
        error_message(args)

#debut du code
requestType()
