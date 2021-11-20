import sys
import string
import time

class color:
    OK = '\033[92m' #VERT -> réponse 
    FAIL = '\033[91m' #ROUGE -> code d'erreur
    RESET = '\033[0m' #GRIS -> remet les couleurs à 0

errors_dict={}
errors_dict[1] = 'ERROR_TYPE_1: Please input a decimal number'
errors_dict[2] = 'ERROR_TYPE_2: Please Type 1 or 2'

def init():
    sys.stdout.write('\r chargement ... |')
    time.sleep(0.2)
    sys.stdout.write('\r chargement .   /')
    time.sleep(0.2)
    sys.stdout.write('\r chargement ..  -')
    time.sleep(0.2)
    sys.stdout.write('\r chargement ... \ ')

def error_message(args): # envoyé avec args, envoie un message d'erreur
    print(color.FAIL, errors_dict[args] ,color.RESET)
    time.sleep(1)
    chooseType()

def req(n):  
    nbr, my_dec = str(n).split(".") 
    nbr = int(nbr) 
    result = (str(bin(nbr))+".").replace('0b','') 
  
    for i in range(30): 
        my_dec = str('0.')+str(my_dec) 
        temp = '%1.20f' %(float(my_dec)*2) 
        my_whole, my_dec = temp.split(".") 
        result += my_whole 
    return result 
  
  
  
def IEEE754(n) :
    signe = 0  
    vInit = n
    if n < 0 :  
        signe = 1
        n = n * (-1)  
    methd =  req (n) 
    ajouterPoint = methd.find('.') 
    ajouter1 = methd.find('1') 
    
    if ajouter1 > ajouterPoint: 
        methd = methd.replace(".","") 
        ajouter1 -= 1
        ajouterPoint -= 1
    if ajouter1 < ajouterPoint:  
        methd = methd.replace(".","") 
        ajouterPoint -= 1
    mantisse = methd[ajouter1+1:] 
    exposants = ajouterPoint - ajouter1 
    bitsexpo = exposants + 127
    bitsexpo = bin(bitsexpo).replace("0b",'')  
    partie3 = mantisse[0:23] 
    
    resultat = str(signe) + bitsexpo.zfill(8) + partie3 
    print(color.OK, vInit, 'équivaut à', resultat, 'avec la norme ', color.FAIL, 'IEEE754',color.RESET,'.' )
    time.sleep(1)
    chooseType()

def somme():
    print(color.OK, "Donnez le chiffre n", color.RESET)
    requestn = input('>>>')
    if (requestn.isdigit()) or (requestn.isdecimal()) or (requestn.isalpha()):
        error_message(1)
    print(color.OK, "Donnez le chiffre m", color.RESET)
    requestm = input('>>>')
    if (requestm.isdigit()) or (requestm.isdecimal()) or (requestm.isalpha()):
        error_message(1)
    
    somme = float(float(requestm) + float(requestn))
    IEEE754(somme)
    


def chooseType():
    n = 0
    m = 0
    print(color.OK, "Que voulez vous faire ?", color.RESET)
    request = input('>>>')
    if request.isdigit():
        request = int(request)
        if request == 1:
            print(color.OK, "Quel nombre flottant voulez vous convertir via la norme IEEE754 ?", color.RESET)
            request = (input(">>>"))
            if (request.isdigit()) or (request.isdecimal()) or (request.isalpha()):
                error_message(1)
            request = float(request)
            print(IEEE754(request))
        if request == 2:
            somme()
        else:
            error_message(2)
chooseType()