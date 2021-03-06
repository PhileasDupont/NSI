import time
import random
from annexes import *
import webbrowser

Version = 3.2

class color:
    OK = '\033[92m'  # VERT -> réponse
    FAIL = '\033[91m'  # ROUGE -> code d'erreur
    RESET = '\033[0m'  # GRIS -> remet les couleurs à 0

def error_message(args, l,old, line0, line1, line2,player, mode, coup): # envoyé avec args, envoie un message d'erreur
    print(color.FAIL, errors[args] ,color.RESET)
    time.sleep(1)
    if old == 'c': 
        chooseType()
    if old == 'x': 
        xplay(line0, line1, line2, mode, coup)
    if old == 'o':
        oplay(line0, line1, line2, mode)
    if old == 'i': 
        increment(l, line0, line1, line2, player, mode)

def check(c, line0, line1, line2,player, mode, coup):
    if c == 'h':
        webbrowser.open('youtube.com')
    if c == 'r':
        if player == 1:
            xplay(line0, line1, line2, mode, coup)
        if player == 2:
            oplay(line0, line1, line2, mode, coup)
    if c == 'q':
        print(color.FAIL, "Merci d'avoir participé !", color.RESET)
        print(color.OK, "Created by ©PhileasDupont", color.RESET)
        print(color.OK, Version, color.RESET)
        time.sleep(1)
        exit()

def checkNull(line0, line1, line2, coup):
    if not(' ' in line1 or ' ' in line2 or ' ' in line0): 
        time.sleep(1)
        print(color.OK, ' LE JEU EST TERMINE !!')
        print(color.OK, 'Il y a eu un ',color.FAIL, 'MATCH NUL', color.OK,' !!', color.RESET)
        print(color.FAIL, 'RETOUR AU DEBUT DU JEU \r \r \r', color.RESET)
        time.sleep(2)
        chooseType()

def checkWinNormal(line0, line1, line2, player, coup):
    if (line0[0] == line1[0] == line2[0] == ('X' or 'O')) or (line0[0] == line0[1] == line0[2] == ('X' or 'O')) or (line1[0] == line1[1] == line1[2] == ('X' or 'O')) or (line0[2] == line1[2] == line2[2] == ('X' or 'O')) or (line2[0] == line2[1] == line2[2] == ('X' or 'O')) or (line0[1] == line1[1] == line2[1] == ('X' or 'O')):
        time.sleep(1)
        print(color.OK, ' LE JEU EST TERMINE !!')
        print(color.OK, 'ce sont les ', color.FAIL,playerdict[player], color.OK, ' qui ont gagné !!', color.RESET)
        print(color.OK, 'en ', color.FAIL,coup, color.OK, ' coups', color.RESET)

        print(color.FAIL, 'RETOUR AU DEBUT DU JEU \r \r \r')
        time.sleep(2)
        chooseType()
    checkWinDiagonal(line0, line1, line2, player, coup)

def checkWinDiagonal(line0, line1, line2, player, coup):
    if (line0[0] == line1[1] == line2[2] == ('X' or 'O')) or (line0[2] == line1[1] == line2[0] == ('X' or 'O')):
        time.sleep(1)
        print(color.OK, ' LE JEU EST TERMINE !!')
        print(color.OK, 'ce sont les ', color.FAIL,playerdict[player], color.OK, ' qui ont gagné !!')
        print(color.OK, 'en ', color.FAIL,coup, color.OK, ' coups', color.RESET)
        chooseType()
    checkNull(line0, line1, line2, coup)


def IAplay(line0, line1, line2, mode, hasPlayed, coup):
    if hasPlayed == False:
        print(color.OK, "c'est à l'ordinateur (", color.FAIL, ' O ',color.OK,") de jouer !", color.RESET)
    l = random.randint(1,3)
    c = random.randint(1, 3)
    player = 2
    time.sleep(1)
    if l == 1:
        selectColumn = c-1 
        if line0[selectColumn] != ' ':
            IAplay(line0, line1, line2, mode, True, coup)
        line0[selectColumn] = 'O'
        print('\n', line0, '\n', line1, '\n', line2)
        checkWinNormal(line0, line1, line2, player, coup)
        mode = 1
        hasPlayed = False
        xplay(line0, line1, line2, mode, coup)
    if l == 2:
        selectColumn = c-1 
        if line1[selectColumn] != ' ':
            IAplay(line0, line1, line2, mode, True, coup)
        line1[selectColumn] = 'O'
        print('\n', line0, '\n', line1, '\n', line2)
        checkWinNormal(line0, line1, line2, player, coup)
        mode = 1
        hasPlayed = False
        xplay(line0, line1, line2, mode, coup)
    if l == 3:
        selectColumn = c-1 
        if line2[selectColumn] != ' ':
            IAplay(line0, line1, line2, mode, True)
        line2[selectColumn] = 'O'
        print('\n', line0, '\n', line1, '\n', line2)
        checkWinNormal(line0, line1, line2, player, coup)
        mode = 1
        hasPlayed = False
        xplay(line0, line1, line2, mode, coup)
    else: 
        error_message(1000, l,'c', line0, line1, line2,player, mode, coup)

def increment(l, line0, line1, line2, player, mode, coup):
    if l == 1:
        print(color.OK, "vous avez choisi la", color.FAIL,
              'première', color.OK, "ligne ", color.RESET)
        print(color.OK, "quelle colonne voulez vous modifier ?", color.RESET)
        c = input('\n >>>')
        check(c, line0, line1, line2,player, mode, coup)
        if c.isdigit():
            c = int(c)
            selectColumn = c-1
            if selectColumn > 4 or selectColumn < 0 or l == '':
                error_message(4, l,'i', line0, line1, line2,player, mode, coup)
            if line0[selectColumn] != ' ':
                print(color.FAIL, 'une entité occupe déjà cette case, merci de recommencer')
                if player == 1:
                    xplay(line0, line1, line2, mode, coup)
                if player == 2:
                    oplay(line0, line1, line2, mode, coup)
            line0[selectColumn] = playerdict[player]
            print('\n', line0, '\n', line1, '\n', line2)
            checkWinNormal(line0, line1, line2, player, coup)
            if mode == 1:
                IAplay(line0, line1, line2, mode, False, coup)
            if player == 1:
                oplay(line0, line1, line2, mode, coup)
            if player == 2:
                xplay(line0, line1, line2, mode, coup)
        else:
            error_message(4, l,'c', line0, line1, line2,player, mode, coup)

    if l == 2:
        print(color.OK, "vous avez choisi la", color.FAIL,
              'deuxième', color.OK, "ligne ", color.RESET)
        print(color.OK, "quelle colonne voulez vous modifier ?", color.RESET)
        c = input('\n >>>')
        check(c, line0, line1, line2,player, mode, coup)
        if (c.isdigit()):
            c = int(c)
            c = c-1
            if c > 4 or c < 0 or l == '':
                error_message(4, l,'i', line0, line1, line2,player, mode, coup)
            if line1[c] != ' ':
                print(color.FAIL, 'une entité occupe déjà cette case, merci de recommencer')
                if player == 1:
                    xplay(line0, line1, line2, mode, coup)
                if player == 2:
                    oplay(line0, line1, line2, mode, coup)
            line1[c] = playerdict[player]
            print('\n', line0, '\n', line1, '\n', line2)
            checkWinNormal(line0, line1, line2, player, coup)
            if mode == 1:
                IAplay(line0, line1, line2, mode, False, coup)
            if player == 1:
                oplay(line0, line1, line2, mode, coup)
            if player == 2:
                xplay(line0, line1, line2, mode, coup)
        else:
            error_message(4, l,'c', line0, line1, line2,player, mode, coup)    

    if l == 3:
        print(color.OK, "vous avez choisi la", color.FAIL,
              'troisième', color.OK, "ligne ", color.RESET)
        print(color.OK, "quelle colonne voulez vous modifier ?", color.RESET)
        c = input('\n >>>')
        check(c, line0, line1, line2,player, mode, coup)
        if (c.isdigit()):
            c = int(c)
            c = c-1
            if c > 4 or c < 0 or l == '':
                error_message(4, l,'i', line0, line1, line2,player, mode, coup)
            if line2[c] != ' ':
                print(color.FAIL, 'une entité occupe déjà cette case, merci de recommencer')
                time.sleep(1)
                if player == 1:
                    xplay(line0, line1, line2, mode, coup)
                if player == 2:
                    oplay(line0, line1, line2, mode, coup)
            line2[c] = playerdict[player]
            print('\n', line0, '\n', line1, '\n', line2)
            checkWinNormal(line0, line1, line2, player, coup)
            if mode == 1:
                IAplay(line0, line1, line2, mode, False, coup)
            if player == 1:
                oplay(line0, line1, line2, mode, coup)
            if player == 2:
                xplay(line0, line1, line2, mode, coup)
        else:
            error_message(4, l,'c', line0, line1, line2,player, mode, coup)

def xplay(line0, line1, line2, mode, coup):
    print(color.OK, "c'est aux ", color.FAIL, " X ", color.OK, " de jouer ! ")
    player = 1
    time.sleep(1)
    print(color.OK, "quelle ligne voulez vous modifier ?", color.RESET)
    l = input('\n >>>')
    if l == 'q':
        print(color.FAIL, "Merci d'avoir participé !", color.RESET)
        print(color.OK, "Created by ©PhileasDupont", color.RESET)
        print(color.OK, Version, color.RESET)
        time.sleep(1)
        exit()
    if (l.isdigit()):
        coup = coup + 1
        l = int(l)
        if l > 3 or l < 1 or l == '':
            error_message(3, l,'x', line0, line1, line2,player, mode, coup)
        increment(l, line0, line1, line2, player, mode, coup)
    else:
        error_message(2, l, 'x', line0, line1, line2,player, mode, coup)

def oplay(line0, line1, line2, mode, coup):
    time.sleep(2)
    print(color.OK, "c'est aux ", color.FAIL, " O ", color.OK, " de jouer ! ")
    player = 2
    mode = 2
    time.sleep(1)
    print(color.OK, "quelle ligne voulez vous modifier ?", color.RESET)
    l = input('\n >>>')
    if l == 'q':
        print(color.FAIL, "Merci d'avoir participé !", color.RESET)
        print(color.OK, "Created by ©PhileasDupont", color.RESET)
        print(color.OK, Version, color.RESET)
        time.sleep(1)
        exit()
    if (l.isdigit()):
        l = int(l)
        if l > 3 or l < 1 or l == '':
            error_message(3, l,'o', line0, line1, line2,player, mode, coup)
        increment(l, line0, line1, line2, player, mode, coup)
    else:
        error_message(2, l,'o', line0, line1, line2,player, mode, coup)

def beginVS(line0, line1, line2, player, mode):
    line0 = [' ', ' ', ' ']
    line1 = [' ', ' ', ' ']
    line2 = [' ', ' ', ' ']

    time.sleep(1)
    print(color.OK, "voici le tableau : ", color.RESET)
    time.sleep(0.5)
    print('\n', line0, '\n', line1, '\n', line2)
    time.sleep(1)
    mode = 2
    coup = 0
    xplay(line0, line1, line2, mode, coup)
    
def beginIA(line0, line1, line2, mode):
    time.sleep(1)
    print(color.OK, "voilà le tableau : ", color.RESET)
    time.sleep(0.5)
    print('\n', line0, '\n', line1, '\n', line2)
    time.sleep(1)
    coup = 0
    xplay(line0, line1, line2, mode, coup)

def chooseType():
    print(Version)
    init()
    line0 = [' ', ' ', ' ']
    line1 = [' ', ' ', ' ']
    line2 = [' ', ' ', ' ']
    print(color.OK, 'que voulez vous faire ?')
    print(color.RESET,'1 -> 1 contre IA \n 2 -> 1 contre 1')
    l = input('>>>')
    if l == 'q':
        print(color.FAIL, "Merci d'avoir participé !", color.RESET)
        print(color.OK, "Created by ©PhileasDupont", color.RESET)
        print(color.OK, Version, color.RESET)
        time.sleep(1)
        exit()
    coup = 0
    player = 1
    if (l.isdigit()):
        l= int(l)
        if l == 1:
            beginIA(line0, line1, line2, 1)
        if l == 2:
            beginVS(line0, line1, line2, 1, 2)

        if l > 2 or l < 1 or l == '':
            error_message(1, l,'c', line0, line1, line2,player, 2, coup)
    else:
        error_message(1, l,'c', line0, line1, line2,player, 2, coup)

chooseType()
