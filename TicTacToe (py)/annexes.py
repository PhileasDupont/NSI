import sys
import string
import time

playerdict = {}
playerdict[1] = 'X'
playerdict[2] = 'O'

errors={}
errors[1] = 'ERROR_TYPE_1 : unavailable request ( you can just type 1 or 2)'
errors[2] = 'ERROR_TYPE_2 : unavailable request ( please input a lettet between 1 and 3 )' 
errors[3] = 'ERROR_TYPE 3 : unavailable line ( please input line between 1 and 3 )'
errors[4] = 'ERROR_TYPE 4 : unavailable column ( please input column between 1 and 3)'
errors[1000] = 'AN ERROR HAS OCCURED -- RESTARING'

def init():
    sys.stdout.write('\r chargement ... |')
    time.sleep(0.2)
    sys.stdout.write('\r chargement .   /')
    time.sleep(0.2)
    sys.stdout.write('\r chargement ..  -')
    time.sleep(0.2)
    sys.stdout.write('\r chargement ... \ \r')  