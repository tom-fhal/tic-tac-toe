
import os
import time
quadrillage = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
Choixjeu = [' ',' '] 
Joueur=1

partieencours = 0
victoire = 1
matchnul = -1
arrêt = 1

game = partieencours 
 

def emplacement(x):    
    if quadrillage[x] == ' ':    
        return True    
    elif quadrillage[x] == 'X' or quadrillage[x]=='O':    
        print("Cet emplacement est déjà occupé !")   

def tableau():    
    print(" %c | %c | %c " % (quadrillage[1],quadrillage[2],quadrillage[3]))
    print("---|---|---")    
    print(" %c | %c | %c " % (quadrillage[4],quadrillage[5],quadrillage[6]))
    print("---|---|---")    
    print(" %c | %c | %c " % (quadrillage[7],quadrillage[8],quadrillage[9]))

def victoire():
    global game 
    if quadrillage[1]==quadrillage[2]==quadrillage[3]!=' ' or quadrillage[4]==quadrillage[5]==quadrillage[6]!=' ' or quadrillage[7]==quadrillage[8]==quadrillage[9]!=' ' or quadrillage[1]==quadrillage[4]==quadrillage[7]!=' ' or quadrillage[2]==quadrillage[5]==quadrillage[8]!=' ' or quadrillage[3]==quadrillage[6]==quadrillage[9]!=' ' or quadrillage[1]==quadrillage[5]==quadrillage[9]!=' ' or quadrillage[3]==quadrillage[5]==quadrillage[7]!=' ':
        game = victoire
    elif(quadrillage[1]!=' ' and quadrillage[2]!=' ' and quadrillage[3]!=' ' and quadrillage[4]!=' ' and quadrillage[5]!=' ' and quadrillage[6]!=' ' and quadrillage[7]!=' ' and quadrillage[8]!=' ' and quadrillage[9]!=' '):    
        game = matchnul  
    else:            
        game = partieencours

print("Tic-Tac-Toe Game")    
print("[1]Joueur 1 [X] VS Joueur 2 [O]")          
print("Chargement...")
print()
print()
print()
print()  


Joueur1=input("Quel pseudo voulez-vous ? : Joueur 1 !\n")
Joueur2=input("Quel pseudo voulez-vous ? Joueur 2 !\n")

while(game == partieencours):       
    tableau()  
    if(Joueur % 2 != 0):    
        print("Joueur 1", Joueur1,"!")    
        repère = 'X'    
    else:    
        print("Joueur 2", Joueur2,"!")    
        repère = 'O'    
    choix = int(input("Choisissez une case entre [1-9] :"))    
    if(emplacement(choix)):    
        quadrillage[choix] = repère    
        Joueur+=1    
        victoire()      
tableau()
   
if(game==matchnul):
    print("Match Nul")    
elif(game==victoire):    
    Joueur-=1    
    if(Joueur%2!=0):
        print("Victoire au Joueur 1", Joueur1, "\n Bravo !!!")    
    else:    
        print("Victoire au Joueur 2", Joueur2, "\n Bravo !!!") 