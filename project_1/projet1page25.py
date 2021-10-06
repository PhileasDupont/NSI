# Projet 1 page 25
# Version 3.0.1

import time
from numbers_dict import *

#classe des couleurs
class basics_colors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def error_message(args):
    print(basics_colors.FAIL, errors_dict[args] ,basics_colors.RESET)
    
#exercice 1 
def decimale_binaire(n):
    req_value_1 = input("donnez un chiffre en base 10 \n >>>")
    n = int(req_value_1)
    if n == 0 or n == 1:
        print(basics_colors.OK, n, " vaut ", n," en toutes les bases ", basics_colors.RESET)
        time.sleep(1)
        requestType()
    if n < 0:
        args = 2
        error_message(args)
        time.sleep(1)
        requestType()

    req_binary(n)
    #end decimale_binaire

def req_binary(n):
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
        time.sleep(3)
        requestType()

# exercice 2
def decimale_hexadecimale(n):
    n = 0
    req_value_1 = input("donnez un chiffre en base 10 \n >>>")
    n = int(req_value_1)

    if n == 0 or n == 1:
        print(basics_colors.OK, n, " vaut ", n," en toutes les bases ", basics_colors.RESET)
        time.sleep(1)
        requestType()
    if n < 0:
        args = 2
        error_message(args)
        time.sleep(1)
        requestType()
    reqBase = 16

    req_hexa(n, reqBase)
    # end decimale_hexadecimale

def req_hexa(n, reqBase):
    
    varListStr = 0
    vInit = n
    binary_list = []
    while n != 0:
        varList = n % reqBase
        n = n // reqBase

        if varList > 9:
            binary_list.insert(0, numbers_dict[varList])
        if varList <= 9:
            binary_list.insert(0, varList)
            
        if n == 0:
            resList = ' ,'.join(map(str,binary_list))
            resListTotal = ''.join(map(str,binary_list)) 
            print(basics_colors.OK, vInit, " en base 10 équivaut à ", resList, " ( ", resListTotal, " ) en base ", reqBase, basics_colors.RESET)
            time.sleep(3)
            requestType()
    
# exercice 3
def base_request(n):
    n = 0
    req_value_1 = input("donnez un chiffre en base 10 \n >>> ")
    vInit = int(req_value_1)
    n = int(req_value_1)

    if n < 0:
        args = 2
        error_message(args)
        time.sleep(1)
        requestType()
    if n == 0 or n == 1:
        print(basics_colors.OK, n, " vaut ", n," en toutes les bases ", basics_colors.RESET)
        time.sleep(1)
        requestType()

    req_value_2 = input("donnez la base en laquelle vous voulez convertir  \n >>>")
    reqBase = int(req_value_2)

    if reqBase <= 1:
        args = 3
        error_message(args)
        time.sleep(1)
        requestType()

    binary_list = []

    if reqBase == 2: #renvoie vers l'exercice de base 2
        req_binary(n)
        requestType()
    if reqBase > 9:
        req_hexa(n, reqBase) #renvoie vers l'exercice de base 16
        requestType()

    while n != 0:
        varList = n % reqBase
        binary_list.insert(0, varList)
        n = n // reqBase

    if n == 0:
        resList = ' ,'.join(map(str,binary_list))
        resListTotal = ''.join(map(str,binary_list)) 
        print(basics_colors.OK, vInit, " en base 10 équivaut à ", resList, " ( ", resListTotal, " ) en base ", reqBase, basics_colors.RESET)
        time.sleep(3)
        requestType()

# demande ce que l'user veut faire 
def requestType():
    request = input("que voulez vous faire ? \n '1' -> conersion décimale vers binaire \n '2' -> conversion décimale vers hexadécimale \n '3' -> conversion décimale vers base demandée \n >>>")
    n = int(request)
    if n < 0 or n > 3:
        args = 1
        error_message(args)
        time.sleep(1)
        requestType()
    if n == 1: 
        decimale_binaire(n) # -> Exercice 1 -> partie du calcul
        return()
    if n == 2:
        decimale_hexadecimale(n) # -> Exercice 2 -> partie du calcul
        return()
    if n == 3:
        base_request(n) # -> Exercice 3 -> partie de demande puis de calcul
        return()

#debut du code
requestType()
