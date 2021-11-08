# annexes 
# v 3.2

import sys
import string
import time

class color:
    OK = '\033[92m' #VERT -> réponse 
    FAIL = '\033[91m' #ROUGE -> code d'erreur
    RESET = '\033[0m' #GRIS -> remet les couleurs à 0


alpha = string.digits + string.ascii_uppercase + string.ascii_lowercase

errors_dict={}
errors_dict[1] = 'ERROR_TYPE_1: Invalid Request'
errors_dict[2] = 'ERROR_TYPE_2: Invalid Number Request (Negative Number)'
errors_dict[3] = "ERROR_TYPE_3: Invalid Base Request (Negative, Null, or '1' Base)"
errors_dict[4] = "ERROR_TYPE_4: Invalid Request (Not a Number, Negative or Decimal)"

def init():
    sys.stdout.write('\r chargement ... |')
    time.sleep(0.2)
    sys.stdout.write('\r chargement .   /')
    time.sleep(0.2)
    sys.stdout.write('\r chargement ..  -')
    time.sleep(0.2)
    sys.stdout.write('\r chargement ... \ ')    


    
