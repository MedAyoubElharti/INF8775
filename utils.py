import random
import time

'''
Fonction pour importer les donnees depuis le fichier exemplaire 
entree: nom du fichier
sortie: nombre_emplacements
        capacite_max
        tableau_r_q tableau de 2 dimentions qui regroupe le revenu r et quantite q pour chaque emplacement
        dictionnaire indexe par le num d'emplacement qui regroupe le revenu r et quantite q pour chaque emplacement par le numero d'emplacement
'''
def read_file(file_name):
    with open(file_name, 'r') as f:  
        data = f.readlines()
        nombre_emplacements = data[0]
        capacite_max = data[-1]
        tableau_r_q = []                     #tableau qui regroupe le revenu r et quantite q pour chaque emplacement(= index +1)
        tableau_r = []
        tableau_q = []
        dict = {}
        emplacement = 1
        for line in data[1:-1]:
            ligne = []
            for e in line.split(" "):
                if e != '' :
                    if '\n' in e :
                        e = e[:-1]
                    ligne.append(int(e))
            #print(ligne[1:])
            tableau_r_q.append(ligne[1:])
            tableau_r.append(ligne[1])
            tableau_q.append(ligne[2])
            dict[emplacement] = ligne[1:] 
            emplacement += 1
        return  nombre_emplacements, capacite_max, tableau_r_q, dict, tableau_r, tableau_q


'''
Fonction qui calcule le rapport R = r/q pour chaque emplacement
entree : tableau de 2 dimentions qui regroupe le nombre d'emplacement, revenu r et quantite q
sortie : liste des rapports r/q 
'''
def rapport_r_q(table):
    liste_rapport = []                             #liste qui regroupe les rapports r/q
    for line in table :
        liste_rapport.append(line[0]/line[1])    #ajout du rapport R = r/q à la liste
    return liste_rapport

#avec les dictionnaires
#entree : dictionnaire qui regroupe le nombre d'emplacement, revenu r et quantite q
#sortie : dictionnaire des rapports r/q 
def drapport_r_q(dict):
    dict_rapport = {}                             
    for e in dict :
        dict_rapport[e] = dict[e][0]/dict[e][1]
    return dict_rapport

'''
Fonction qui calcule la probabilite pi = Ri/sum(ri)
entree : liste des rapports r/q
sortie : liste des probabilites pi pour chaque emplacement
'''
def probabilite(liste_rapport):
    liste_probabilite = []               # liste qui regroupe les probabiltes calculees pour chaque emplacement
    somme_rapports = sum(liste_rapport)   # variable qui contient la sommes des rapports
    for R in liste_rapport :
        liste_probabilite.append(R/somme_rapports)
    return liste_probabilite

#avec les dictionnaires
#entree : disctionnaire des rapports r/q
#sortie : dictionnaire des probabilites pi pour chaque emplacement 

def dprobabilite(dict_rapport):
    dict_probabilite = {}                         # dict qui regroupe les probabiltes calculees pour chaque emplacement
    somme_rapports = sum(dict_rapport.values())   # variable qui contient la sommes des rapports
    for e in dict_rapport :
        dict_probabilite[e] = dict_rapport[e]/somme_rapports
    return dict_probabilite

'''
Fonction qui calcule la fonction de repartition (probabilites cumulatives)
entree : liste des probabilites pi
sortie : liste des probabilites cumulatives
'''
def repartition(liste_probabilite):
    liste_repartition = []
    probabilite_precedente = 0
    for p in liste_probabilite :
        probabilite_precedente += p
        liste_repartition.append(probabilite_precedente)

    return liste_repartition

# avec les dictionnaires
# entree : liste des probabilites pi
# sortie : liste des probabilites cumulatives

def drepartition(dict_probabilite):
    dict_repartition = {}
    probabilite_precedente = 0
    for e in dict_probabilite :
        probabilite_precedente += dict_probabilite[e]
        dict_repartition[e] = probabilite_precedente
    return dict_repartition

'''
Fonction qui retourne le numero de l'emplacement a choisir a partir d'un nombre aleatoire entre 0 et 1 
entree : *liste de disribution des probabilites
         *valeur du nombre aleatoire
sortie : le numero de l'emplacement convenable 
'''
def numero_emplacement(liste_repartition, nombre_aleatoire):

    for i in range(len(liste_repartition)) :
        if nombre_aleatoire < liste_repartition[i]:
            return i + 1


def dnumero_emplacement(dict_repartition, nombre_aleatoire):

    keys_list = list(dict_repartition.keys())

    for i in range(len(keys_list)):
        if nombre_aleatoire < dict_repartition[keys_list[i]]:
            return keys_list[i]
    '''
    for e in dict_repartition :
        if nombre_aleatoire < dict_repartition[e]:
            index = dict_repartition.index(e)
            return e + 1
    '''

'''
Fonction pour executer l'algo de glouton probabiliste
Entree: nom du fichier exemplaire
Sortie: liste des numeros des emplacements pris
'''
def glouton_probabliste_execute(file_name):

    #start
    debut = time.time()
    dict_r_q = read_file(file_name)[3]
    capacite_max = int(read_file(file_name)[1])
    capacite_dispo = capacite_max
    emplacement_pris =[]
    revenu = 0
    i = 0
    while capacite_dispo>0 and i < len(dict_r_q) :
        i+=1
        dict_rapport = drapport_r_q(dict_r_q)
        # print("__________________________________________________________")
        # print("i = ", i)
        # print("----------------------------------------------------------")
        # print("len dict_r_q: ", len(dict_r_q))
        # for key, value in dict_r_q.items() : print(key, value)
        dp = dprobabilite(dict_rapport)
        dict_repartition = drepartition(dp)
        # print("######################## REPARTITION #######################")
        # print("len Repartition", len(dict_repartition))
        # for key, value in dict_repartition.items() : print(key, value)
        # print("#####################################################################")
        random_number = random.random()
        # print("---------Random---------", random_number)
        demplacement = dnumero_emplacement(dict_repartition, random_number)
        # print("emplacement: ", demplacement)
        if dict_r_q[demplacement][1] < capacite_dispo:
            capacite_dispo -= int(dict_r_q[demplacement][1])
            emplacement_pris.append(demplacement)
            revenu += int(dict_r_q[demplacement][0])
            dict_r_q.pop(demplacement)
        #print("capa dispo", capacite_dispo)
        if capacite_dispo <0 : break
        
    #end
    fin = time.time()

    return emplacement_pris, fin-debut, revenu #execution_time

def programmation_dynamique(file_name):
    debut = time.time()
    capacite_max = read_file(file_name)[1]
    W = int(capacite_max)
    tableau_r = read_file(file_name)[4]
    tableau_q = read_file(file_name)[5]
    n=len(tableau_r)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(W + 1): 
            if i == 0 or j == 0: 
                table[i][j] = 0
            elif tableau_q[i-1] <= j: 
                table[i][j] = max(tableau_r[i-1]  
+ table[i-1][j-tableau_q[i-1]],  table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 

    fin = time.time()            
   
    return table[n][W], fin - debut

# verifier si la somme des probabilites = 1
#file = "exemplaires\WC-100-10-01.txt"
#capacite_max = read_file(file)[1]
#tableau_r_q = read_file(file)[2]
#dict_r_q = read_file(file)[3]

# liste_rapport = rapport_r_q(tableau_r_q)
# #dict_rapport = drapport_r_q(dict_r_q)

# print(sum(dict_rapport.values()))

# p = probabilite(liste_rapport)
# dp = dprobabilite(dict_rapport)

# liste_repartition = repartition(p)
# dict_repartition = drepartition(dp)

# emplacement = numero_emplacement(liste_repartition, 0.5)
# demplacement = dnumero_emplacement(dict_repartition, 0.5)


# pris = glouton_probabliste_execute(file)
# capacite = 0
# print(pris)
# for e in pris :
#     capacite += read_file(file)[3][e][1]
# print(capacite)

# print(emplacement)

# '''
# for i in range(len(liste_repartition)):
#     print(i+1, liste_repartition[i])
#     '''
# for i in range(1000):
#     value = random.random()
#     if value > 1 : print(">1")

# capacite_dispo = capacite_max
# while capacite_dispo > 0 :
#     p = probabilite(rapport)
#     liste_repartition = repartition(p)
#     random_number = random.random()



#print(tableau_r_q)
# print(dict_r_q)
# print(emplacement)
# print(demplacement)
