from utils import *


##################################################
###   ######                                   ### 
###     ##    1er ALGO : GLOUTON PROBABILISTE  ###
###   ######                                   ###
##################################################


'''
1 - Execution de l'algo en utilisant un fichier exemplaire de taille 100  
'''
file = "exemplaires\WC-100-10-01.txt"
pris = glouton_probabliste_execute(file)
capacite = 0
print(pris)
for e in pris :
    capacite += read_file(file)[3][e][1]
print(capacite)