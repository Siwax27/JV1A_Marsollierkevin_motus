import random
from colorama import init
from colorama import Fore, Back, Style
init()

#afficher la grille
def affichegrille(grille):
    for i in range (0,24,6):
        print(grille[i],grille[i+1],grille[i+2], grille[i+3],grille[i+4],grille[i+5])

#afficher la couleur
bienPlacer = (Back . RED + "a","b","y","e","r","o","n","s","j","g","c","u","p","k","i","t")
malPlacer = (Back . YELLOW + "a","b","y","e","r","o","n","s","j","g","c","u","p","k","i","t")
pasDedans = (Back . BLUE + "d","f","h","l","m","q","v","w","x","z")

#mot random 
motrandom = ["aboyer","bornes","jargon","occupe","kiyoko","target"] 

#choisir un des mot random
mot = random.choice(motrandom)
motproposer = " "
#implemanter le mot random a une variable
if mot == 0:
    mot = motrandom[0]
if mot == 1:
    mot = motrandom[1]
if mot == 2:
    mot = motrandom[2]
if mot == 3:
    mot = motrandom[3]
if mot == 4:
    mot = motrandom[4]
if mot == 5:
    mot = motrandom[5]

#nombre de tour
tour = 5

#nombre de case dans le table
tableau = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_",]

#code principale
while tour >0:
    affichegrille(tableau)
    tour = tour-1
    proposition = input("veuillez choisir un mot : \n")
    if tour == 4:
        tableau[0] = proposition
        tableau[1] = ""
        tableau[2] = ""
        tableau[3] = ""
        tableau[4] = ""
        tableau[5] = ""
    if tour == 3:
        tableau[6] = proposition
        tableau[7] = ""
        tableau[8] = ""
        tableau[9] = ""
        tableau[10] = ""
        tableau[11] = ""
    if tour == 2:
        tableau[12] = proposition
        tableau[13] = ""
        tableau[14] = ""
        tableau[15] = ""
        tableau[16] = ""
        tableau[17] = ""
    if tour == 1:
        tableau[18] = proposition
        tableau[19] = ""
        tableau[20] = ""
        tableau[21] = ""
        tableau[22] = ""
        tableau[23] = ""
    if proposition == mot:
        print("bravo vous avec trouver le mot")
        break
    affichegrille(tableau)    

