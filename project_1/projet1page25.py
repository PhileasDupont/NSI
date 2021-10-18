# Projet 1 page 25
# Version 4.1
# Version en cours de documentation

import time
from numbers_dict import *
import webbrowser

#classe des couleurs
class basics_colors:
    OK = '\033[92m' #VERT -> réponse 
    FAIL = '\033[91m' #ROUGE -> code d'erreur
    RESET = '\033[0m' #GRIS -> remet les couleurs à 0

def error_message(args): # envoyé avec args, envoie un message d'erreur
    print(basics_colors.FAIL, errors_dict[args] ,basics_colors.RESET)
    time.sleep(1)
    requestType()

def verif(request):
    if request == 'a' or request == 'again':
        print(basics_colors.OK, ' retour au début ...', basics_colors.RESET)
        time.sleep(0.5)
        requestType()
    if request == 'help' or request == 'h':
        print(basics_colors.OK,"redirection sur le GitHub ...", basics_colors.RESET)
        webbrowser.open('https://github.com/PhileasDupont/NSI/blob/main/project_1/')
        time.sleep(2)
        requestType()
    if request == 'q' or request == 'quit':
        print(basics_colors.FAIL, "Merci d'avoir participé !", basics_colors.RESET)
        print(basics_colors.OK, "Created by ©PhileasDupont", basics_colors.RESET)
        time.sleep(1)
        exit()

def binaire_hexa(n, reqBase): # envoyé grace à requestType()
    request = input("donnez un chiffre en base 10 \n >>>")
    verif(request)
    if ( request.isdigit()):
        n = int(request)
        if n == 0 or n == 1: # valeurs par défaut
            print(basics_colors.OK, n, " vaut ", n," en toutes les bases ", basics_colors.RESET)
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
            print(basics_colors.OK, vInit, " en base 10 équivaut à ", resList, " ( ", resListTotal, " ) en base ", reqBase, basics_colors.RESET)
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
            print(basics_colors.OK, n, " vaut ", n," en toutes les bases ", basics_colors.RESET)
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
    print(basics_colors.OK, "debut du programme ...", basics_colors.RESET)
    time.sleep(1)
    print("que voulez vous faire ? \n '1' -> conersion décimale vers binaire \n '2' -> conversion décimale vers hexadécimale \n '3' -> conversion décimale vers base demandée \n A n'importe quel moment tapez", basics_colors.FAIL, ' a ', basics_colors.RESET, "pour", basics_colors.FAIL, " RECOMMENCER ", basics_colors.RESET, ", tapez", basics_colors.FAIL, " h ", basics_colors.RESET, "pour être", basics_colors.FAIL, " redirigé vers la page d'aide ", basics_colors.RESET, "ou tapez", basics_colors.FAIL, " q ", basics_colors.RESET, "pour", basics_colors.FAIL, " QUITTER", basics_colors.RESET)
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
