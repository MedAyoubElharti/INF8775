import os
from tabulate import tabulate

from utils import *
from main import main



'''
Fonction qui calcule le temps d'execution moyen d'un algorithme pour une taille d'exemplaire donnée n et série max s
'''
def temps_moyen(algo, n, s=10):
    
    file_list = []                           #liste pour regrouper tous les fichiers qui ont la taille et la série souhaitées  
    for file in os.listdir("./exemplaires"):
        #chaine ="WC-"+str(n)+"-"+str(s)+"-"
        chaine ="WC-"+str(n)+"-"       #identifier les fichiers qui ont la taille souhaitée et la série souhaitées à partir de leurs noms
        if chaine in file :
            #print(file)
            file_list.append(file)
    print(file_list)
    temps_moyen = 0
    for file in file_list :
        temps_moyen += main(algo, file)[1]
    temps_moyen = temps_moyen/len(file_list)
    #print("TEMPS_MOYEN ", temps_moyen)
    return temps_moyen

# En fction de serie aussi  ??????? SOS
# '''
# Fonction qui prend en argument une liste des tailles d'exemplaire et retourne
# une liste de couple temps_moyen en fonction de la taille d'exemplaire
# '''
def liste_temps_moyen_en_fct_taille(algo, tailles):
    liste = []
    for taille in tailles:
        #print(taille)
        liste.append((temps_moyen(algo, taille),taille))
    return liste




################################################################################################################
######     
  ##                                         Présentation des résultats	  
  ##                                       Sous forme de tableau et graphe 
######
###############################################################################################################  

tailles = [100, 1000, 10000]
x_val = tailles

# Liste de couple temps_moyen en fonction de la taille d'exemplaire pour l'algo Glouton probabiliste
list_glouton_prob = liste_temps_moyen_en_fct_taille("Glouton_Prob", tailles)
y_val_glouton_prob = [x[0] for x in list_glouton_prob]

#Regroupement des resultats sous forme de tuple [Taille, Temps_moyen_glouton_prob (s), Temps_moyen_prog_dyn (s), Temps_moyen_amelio_local (s)]
Liste_resultats = []
for i in range(len(x_val)) :
    tuple = [x_val[i], y_val_glouton_prob[i] ] #, y_val_dpr3[i], y_val_dpr15[i]]
    Liste_resultats.append(tuple)

# Présentation des résultats sous forme de tableau

#tableau = tabulate(Liste_resultats, headers=['Taille', 'Temps_moyen_BF (s)', 'Temps_moyen_DPR3 (s)', 'Temps_moyen_DPR15 (s)'], tablefmt = 'fancy_grid')

tableau = tabulate(Liste_resultats, headers=['Taille', 'Temps_moyen_Glouton_probabiliste (s)'], tablefmt = 'fancy_grid')
print(tableau)
with open("tableau.txt", 'w', encoding="utf-8") as f:
    f.write(tableau)