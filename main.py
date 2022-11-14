from utils import *
import sys


'''
Fonction principale qui prend en entrée le nom de l'algo à utiliser et le fichier d'exemplaire 
et retourne le résultat ainsi que le temps d’exécution
'''

def main(algo, file_name):

    file_path = "./exemplaires/" + file_name
    if algo == "Glouton_Prob":
        # Exécuter l'algorithme force brute
        pris, duree, revenu = glouton_probabliste_execute(file_path)
        #print("Temps : ", time_BF)
        return pris, duree, revenu
    
    elif algo == "Prog_Dyn":
        return

    elif algo == "Amelio_loc":
        return

'''
Fonction pour interagir avec l'interface demandée
'''
# def main_interface(argv):

#     file_name = argv[2]
#     POINTS = import_points(file_name)
#     sorted_points_x = sorted(POINTS, key=lambda x: x[0])
#     sorted_points_y = sorted(POINTS, key=lambda x: x[1])

#     if argv[1] == "brute":
#         time_BF, dist_min_BF = execute_brute_force(sorted_points_x)
#         if "-t" in argv :
#             print("Temps : ", time_BF*1000)
#         if "-p" in argv :
#             print("Distance min : ", dist_min_BF)

#     elif argv[1] == "recursif":
#         SEUIL_DPR = 3
#         time_dpr, dist_min_dpr = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_DPR)
#         if "-t" in argv :
#             print("Temps : ", time_dpr*1000)
#         if "-p" in argv :
#             print("Distance min : ", dist_min_dpr)
    
#     elif argv[1] == "seuil":
#         SEUIL_DPR = 15
#         time_dpr_s, dist_min_dpr_s = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_DPR)
#         if "-t" in argv :
#             print("Temps : ", time_dpr_s*1000)
#         if "-p" in argv :
#             print("Distance min : ", dist_min_dpr_s)    

# if __name__ == "__main__":
#     main_interface(sys.argv)



##################################################
###   ######                                   ### 
###     ##    1er ALGO : GLOUTON PROBABILISTE  ###
###   ######                                   ###
##################################################


'''
1 - Execution de l'algo en utilisant un fichier exemplaire de taille 100  
'''
if __name__ == "__main__":
    for i in range(10):
        file = "WC-100-10-01.txt"
        algo = "Glouton_Prob"
        path = "./exemplaires/"+file
        pris, duree, revenu1 = main(algo, file)
        capacite = 0
        revenu = 0
        print("############## ", i, " ####################")
        print("Emplacements pris", pris)
        for e in pris :
            capacite += read_file(path)[3][e][1]
            revenu += read_file(path)[3][e][0]
    
        print("capacite", capacite)
        print("revenu", revenu, revenu1)
        print("duree", duree)
        print("-------------------------------------------")