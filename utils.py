import random

'''
Fonction pour importer les donnees depuis le fichier exemplaire 
entree: nom du fichier
sortie: nombre_emplacements
        capacite_max
        tableau_r_q tableau de 2 dimentions qui regroupe le revenu r et quantite q pour chaque emplacement
        dictionnaire indexe qui regroupe le revenu r et quantite q pour chaque emplacement par le numero d'emplacement
'''
def read_file(file_name):
    with open(file_name, 'r') as f:  
        data = f.readlines()
        nombre_emplacements = data[0]
        capacite_max = data[-1]
        tableau_r_q = []                     #tableau qui regroupe le revenu r et quantite q pour chaque emplacement(= index +1)
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
            dict[emplacement] = ligne[1:] 
            emplacement += 1
        return  nombre_emplacements, capacite_max, tableau_r_q, dict


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
#entree : disctionnaire qui regroupe le nombre d'emplacement, revenu r et quantite q
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

  
# verifier si la somme des probabilites = 1
file = "exemplaires\WC-100-10-01.txt"
capacite_max = read_file(file)[1]
tableau_r_q = read_file(file)[2]
dict = read_file(file)[3]

rapport = rapport_r_q(tableau_r_q)
drapport = drapport_r_q(dict)

# p = probabilite(rapport)
# liste_repartition = repartition(p)

# emplacement = numero_emplacement(liste_repartition, 0.5)

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
print(dict)
for i in dict :
    print(drapport[i] == rapport[i-1])
