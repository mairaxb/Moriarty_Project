# -*- coding: utf-8 -*-
import random
joueur=''
p=''

#--------------------------------------------------------
def display_menu():
     print "############################""\n Menu Principal \n" "############################"
     print "Tapez 1 pour jouer en mode joueur contre joueur."
     print "Tapez 2 pour jouer en mode joueur contre ordinateur."
     print "Tapez 3 pour afficher les regles du jeu."
     print "Tapez 0 pour quitter."
     
#--------------------------------------------------------
def regles():
    print "Les regles du jeu sont les suivantes: \n"
    print "1. Regles generales"
    print " - le jeu est compose de 2 joueurs"
    print " - un joueur est l activateur, l autre est l inhibiteur"
    print " - une case contient un pion proteine activee, un pion proteine inhibee ou bien est vide"
    print " - les joueurs disposent d un ensemble de 64 pions proteines"
    print " - la partie debute avec 2 pions proteines actives et 2 pions proteines inactives"
    print " - la partie se deroule selon un cycle ou chaque joueur joue tour a tour "
    print " - la partie est terminee quand l un des joueurs ne peut plus pose de pions"
    print " - la partie est remportee quand un joueur obtient la majorite apres comptage des pions proteines \n"
    print "1.2 Regles specifiques aux proteines"
    print " - la couleur verte represente la proteine active et la couleur rouge la proteine inactive"
    print " - quand un ou plusieurs pions proteines inhibees sont encadrees par 2 pions proteines activees, ils deviennent activees, et inversement"
    print " - l encadrement des pions proteines peut se faire de facon horizontale, verticale ou diagonale"
    print " - un changement d etat d'une proteine est imperative avant de pouvoir poser un autre pion"


#--------------------------------------------------------
#Initialisation du plateau de jeu
plateau = []
for row in range (9):
    plateau.append([])
    for col in range(9):
        plateau[row].append('.')
        
plateau[0]=[" ","1","2","3","4","5","6","7","8"]

plateau[1][0]='1'
plateau[2][0]='2'
plateau[3][0]='3'
plateau[4][0]='4'
plateau[5][0]='5'
plateau[6][0]='6'
plateau[7][0]='7'
plateau[8][0]='8'
 
#--------------------------------------------------------   
def initialisation(plateau,joueur):    
    plateau[4][4]='\033[1;32mV\033[1;m'
    plateau[4][5]='\033[1;31mR\033[1;m'
    plateau[5][4]='\033[1;31mR\033[1;m'
    plateau[5][5]='\033[1;32mV\033[1;m'
            
    joueur='\033[1;32mV\033[1;m'
    return joueur

#--------------------------------------------------------
def display_plateau (plateau):
    for row in plateau :
        print ( " ".join(row))   

#--------------------------------------------------------
#Permet de verifier que le joueur joue bien dans le plateau
def in_plateau(x,y):
    return x > 0 and x < 9 and y >0 and y <9  

#--------------------------------------------------------
#Demande au joueur ou il veut poser son pion
def print_coord():
     print "veuillez inserer les coordonnes pour ajouter une nouvelle proteine" 
     value_x=input("Coordonnees de x : \n")
     value_y=input("Coordonnees de y : \n")
     return value_x, value_y
    
#--------------------------------------------------------
def belong_joueur(joueur,plateau,x,y):
    return plateau[x][y]==joueur

#--------------------------------------------------------
#Permet de placer un nouveau pion par le joueur
def make_move(plateau,joueur):
    if joueur=='\033[1;32mV\033[1;m':
        p='V'
    if joueur=='\033[1;31mR\033[1;m':
        p='R'
    check= True
    while check :
        print "C est le tour du joueur",p
        x, y = print_coord()      
                                 
        if in_plateau(x,y): 
            empty= check_empty(plateau,x,y)
            if empty and flip(plateau,x,y,joueur,False) :
                plateau[x][y]= joueur
                flip(plateau,x,y,joueur,True)
                check=False
    
        if check:
            print "Erreur, veuillez recommencer cette position n'est pas valide"

#--------------------------------------------------------
#Permet de placer un nouveau pion par ordinateur 
def make_move_computer(plateau,joueur):
    check= True
    while check :
        a = random.randint(1,8)
        b = random.randint(1,8)
        x = int(a)
        y = int(b)
        
        if in_plateau(x,y):
            empty= check_empty(plateau,x,y)
            if empty and flip(plateau,x,y,joueur,False) :
                plateau[x][y]= joueur
                flip(plateau,x,y,joueur,True)
                check=False                        
        if check:
            return make_move_computer(plateau,joueur)
        
#--------------------------------------------------------
#Permet de verifier toutes les positions
def left(y):
    return y-1
def up(x):
    return x-1
def right(y):
    return y+1
def down (x):
    return x+1

#--------------------------------------------------------          
def flip(plateau,x,y,joueur,change):
    switch=False
    for i in range (8):
        coordX=[]
        coordY=[]
        x1=x
        y1=y    
        check2=True
        while check2:   
            if i ==0:
                x1=up(x1)
            if i==1:
                x1=down (x1)
            if i==2:
                y1=left(y1)
            if i==3:
                y1=right(y1)
            if i==4:
                x1=up(x1)
                y1=right(y1)
            if i==5:
                x1=up(x1)
                y1=left(y1)
            if i==6:
                x1=down (x1)
                y1=right(y1)
            if i==7:
                x1=down (x1)
                y1=left(y1)
            
            check2 = in_plateau(x1,y1) and not check_empty(plateau,x1,y1)
            
            if check2:            
                if belong_joueur(joueur,plateau,x1,y1):
                    for i in range (len(coordX)):
                        if change :
                            x2=coordX[i]
                            y2=coordY[i]
                            plateau[x2][y2]=joueur
                        switch=True
                    check2=False
                else:                   
                    coordX.append(x1)
                    coordY.append(y1)               
    return switch
    
#--------------------------------------------------------
#Verifie si une case est vide ou non 
def check_empty(plateau,x,y):
    if plateau[x][y]=='.':
       return True
    else:
       return False
    
#--------------------------------------------------------
#Verifie si le joueur peut joueur
def legal_move(joueur):
    for a in range (plateau):
        for b in range (plateau):
            if plateau[a][b]=='.':
                if flip(plateau,x,y,joueur,False):                
                    return True              
    return False            

#--------------------------------------------------------
#Permet de changer de couleur a chaque tour
def change_joueur(joueur):  
    if joueur =='\033[1;32mV\033[1;m':        
        return '\033[1;31mR\033[1;m'    
    if joueur =='\033[1;31mR\033[1;m':
        return '\033[1;32mV\033[1;m'

#--------------------------------------------------------
#Verifie si le plateau contient toujours des cases vides 
def check_plateau (plateau) : 
    for raw in plateau :
        for col in raw:
            if col == '.':
                return True
    return False

#--------------------------------------------------------
def get_score(plateau):
    Vscore = 0
    Rscore = 0
    for x in range(8):
        for y in range(8):
            if plateau[x][y]=='\033[1;32mV\033[1;m':
                Vscore += 1
            if plateau[x][y]=='\033[1;31mR\033[1;m':
                Rscore += 1
    print "Score V:", Vscore, "Score R:", Rscore
    return {'V': Vscore, 'R': Rscore}
        


#--------------------------------------------------------
#Programme principal
print "Bienvenue dans le jeu Moriarty. \n"

while True:
    display_menu()
    answer = input()
    joueur=initialisation(plateau,joueur)
    if answer==0 :
        break
    elif answer==1 :
        while check_plateau(plateau):
            display_plateau(plateau)
            get_score(plateau)
            make_move(plateau,joueur)
            joueur=change_joueur(joueur)
    elif answer==2 :
        while check_plateau(plateau):
            display_plateau(plateau)
            get_score(plateau)
            make_move(plateau,joueur)
            joueur=change_joueur(joueur)
            display_plateau(plateau)
            get_score(plateau)
            make_move_computer(plateau,joueur)
            joueur=change_joueur(joueur)      
    elif answer==3:
        regles()        
    else:
        print "Erreur."
print "Au revoir."
        
     

     
    

