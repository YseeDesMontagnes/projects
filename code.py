#!/usr/bin/env python
# coding: utf8
from random import randrange, randint
import networkx as nx
import matplotlib.pyplot as plt

graphe = nx.DiGraph()

nomsNoeudsFixes = ['DET', 'FIX', 'RES', 'LOS', 'PHY']

"""déclaration de certaines variables"""
nbNodes4 = {}
nbNodes4['n1'] = 0
nbNodes4['n2'] = 0
nbNodes4['n3'] = 0
nbNodes4['n4'] = 0

nbNodes5 = {}
nbNodes5['n1'] = 0
nbNodes5['n2'] = 0
nbNodes5['n3'] = 0
nbNodes5['n4'] = 0
nbNodes5['n5'] = 0

nbArcs4 = {}
nbArcs4['k12'] = 0
nbArcs4['k23'] = 0
nbArcs4['k34'] = 0
nbArcs4['k13'] = 0
nbArcs4['k24'] = 0
nbArcs4['k14'] = 0
nbArcs4['loops'] = 0
nbArcs4['k_'] = 0

nbArcs5 = {}
nbArcs5['k12'] = 0
nbArcs5['k13'] = 0
nbArcs5['k14'] = 0
nbArcs5['k15'] = 0
nbArcs5['k23'] = 0
nbArcs5['k24'] = 0
nbArcs5['k25'] = 0
nbArcs5['k34'] = 0
nbArcs5['k35'] = 0
nbArcs5['k45'] = 0
nbArcs5['loops'] = 0
nbArcs5['k_'] = 0

nodes=[]
arcs=[]

graph=[nodes,arcs]

class node:
    """Descriptif de chaque noeud"""
    def __init__(self,name,pred,succ,level):
        self.name = name
        self.pred = pred
        self.succ = succ
        self.level = level



def generate(n,t):
    if t == 4:
        nbNodes4 = levels_4(n)
        nbArcs4 = edges_4(nbNodes4)
        generate_4(nbNodes4,nbArcs4)
        fichier_4(n,nodes,nbNodes4,nbArcs4)
    elif t == 5:
        levels_5(n)
        edges_5(n)
        generate_5(nbNodes5,nbArcs5)

def generate_density(n,t):
    pass


def levels_4(n): #génère un nb aléatoire de noeuds par niveau, les noeuds fixes ne sont pas comptés
    bool = True

    while bool:
        nbNodes4['n1'] = randrange(n+1) + 2 #compte les noeuds DET et PHY
        nbNodes4['n2'] = randrange(n+1)
        nbNodes4['n3'] = randrange(n+1)
        nbNodes4['n4'] = randrange(n+1)

        if (((nbNodes4['n1'] - 2) + nbNodes4['n2'] + nbNodes4['n3'] + nbNodes4['n4'] == n) and (nbNodes4['n2'] >= nbNodes4['n3']) and (nbNodes4['n3'] >= nbNodes4['n1']) and (nbNodes4['n1'] >= nbNodes4['n4']) and (nbNodes4['n4'] > 0)): #conditions d'arrêt de la boucle, manière peu optimisée de faire mais qui fonctionne
            bool = False

    return nbNodes4


"""def levels_5(n):
    while nbNodes['n1']+nbNodes5['n2']+nbNodes5['n3']+nbNodes5['n4']+nbNodes5['n5'] != n:
        nbNodes5['n1'] = randrange(n+1)
        nbNodes5['n2'] = randrange(n+1)
        nbNodes5['n3'] = randrange(n+1)
        nbNodes5['n4'] = randrange(n+1)
        nbNodes5['n5'] = randrange(n+1)

    return nbNodes5"""

def edges_4(nbNodes4): #génère un nombre aléatoire d'arcs d'un niveau n vers un niveau m (knm), de boucles (loops) et d'autres arcs (k_)
    nbArcs4['k12'] = randrange(min(nbNodes4['n1'],nbNodes4['n2']) + 1)
    nbArcs4['k23'] = randrange(min(nbNodes4['n2'],nbNodes4['n3']) + 1)
    nbArcs4['k34'] = randrange(min(nbNodes4['n3'],nbNodes4['n4']) + 1)
    nbArcs4['k13'] = randrange(min(nbNodes4['n1'],nbNodes4['n3']) + 1)
    nbArcs4['k24'] = randrange(min(nbNodes4['n2'],nbNodes4['n4']) + 1)
    nbArcs4['k14'] = 0 #tout le temps 0
    #nbArcs4['loops'] = 0 #tout le temps 0, en vrai non mais là c'est plus simple
    nbArcs4['loops'] = randrange(3)
    #nbArcs4['k_'] = randrange(max(nbNodes4.values()) + 1)
    nbArcs4['k_'] = randrange(sum(nbNodes4.values()) + 3)

    return nbArcs4


def edges_5(nbNodes5):
    nbArcs5['k12'] = 0
    nbArcs5['k13'] = 0
    nbArcs5['k14'] = 0
    nbArcs5['k15'] = 0
    nbArcs5['k23'] = 0
    nbArcs5['k24'] = 0
    nbArcs5['k25'] = 0
    nbArcs5['k34'] = 0
    nbArcs5['k35'] = 0
    nbArcs5['k45'] = 0
    nbArcs5['loops'] = 0
    nbArcs5['k_'] = 0

    return nbArcs5

def generate_4(nbNodes4,nbArcs4):

    nodes.append(node('FIX',list(),list(),0)) #remplie nodes avec les points fixes
    nodes.append(node('DET',list(),list(),1)) #1
    nodes.append(node('PHY',list(),list(),1)) #2
    for i in range(0,(nbNodes4['n1'] - 2)): #remplie le reste, par niveau
        nodes.append(node(str(i),list(),list(),1))
    for i in range(int(nodes[-1].name) + 1, nbNodes4['n2'] + int(nodes[-1].name) + 1):
        nodes.append(node(str(i),list(),list(),2))
    for i in range(int(nodes[-1].name) + 1, nbNodes4['n3'] + int(nodes[-1].name) + 1):
        nodes.append(node(str(i),list(),list(),3))
    for i in range(int(nodes[-1].name) + 1, nbNodes4['n4'] + int(nodes[-1].name) + 1):
        nodes.append(node(str(i),list(),list(),4))
    nodes.append(node('LOS',list(),list(),6))
    nodes.append(node('RES',list(),list(),7))

    posFix = 0
    posDet = 1
    posPhy = 2
    posLos = sum(nbNodes4.values()) + 1
    posRes = sum(nbNodes4.values()) + 2 #dernière valeur du tableau nodes


    nodes[posFix].pred.append(None) #FIX est une racine
    nodes[posFix].succ.append(nodes[posPhy].name) #PHY succède à FIX
    nodes[posPhy].pred.append(nodes[posFix].name) #PHY précède FIX
    nodes[posPhy].succ.append(nodes[posDet].name) #DET succède à PHY
    nodes[posPhy].succ.append(nodes[posLos].name) #LOS succède à PHY
    nodes[posPhy].succ.append(nodes[posRes].name) #RES succède à PHY
    nodes[posDet].pred.append(nodes[posPhy].name) #DET précède PHY
    nodes[posLos].pred.append(nodes[posPhy].name) #LOS précède PHY
    nodes[posRes].pred.append(nodes[posPhy].name) #RES précède PHY

    i_deb = 1 + nbNodes4['n1']
    deb_origin = 1
    for i in range(i_deb, i_deb + nbNodes4['n2']): #attribue une origine à chaque noeud du rang2
        origin = randrange(deb_origin,deb_origin + nbNodes4['n1'])
        nodes[origin].succ.append(nodes[i].name)
        nodes[i].pred.append(nodes[origin].name)

    i_deb += nbNodes4['n2']
    deb_origin += nbNodes4['n1']
    for i in range(i_deb, i_deb + nbNodes4['n3']): #attribue une origine à chaque noeud du rang3
        origin = randrange(deb_origin,deb_origin + nbNodes4['n2'])
        nodes[origin].succ.append(nodes[i].name)
        nodes[i].pred.append(nodes[origin].name)

    i_deb += nbNodes4['n3']
    deb_origin += nbNodes4['n2']
    for i in range(i_deb, i_deb + nbNodes4['n4']): #attribue une origine à chaque noeud du rang4
        origin = randrange(deb_origin,deb_origin + nbNodes4['n3'])
        nodes[origin].succ.append(nodes[i].name)
        nodes[i].pred.append(nodes[origin].name)

    #ajout des arcs supplémentaires entre niveau 1 et 2
    deb_origin = 1
    deb_destination = deb_origin + nbNodes4['n1']
    for i in range(nbArcs4['k12']):
        origin = randrange(deb_origin,deb_destination)
        destination = randrange(deb_destination,deb_destination + nbNodes4['n2'])
        nodes[origin].succ.append(nodes[destination].name)
        nodes[destination].pred.append(nodes[origin].name)

    #ajout des arcs supplémentaires entre niveau 2 et 3
    deb_origin += nbNodes4['n1']
    deb_destination = deb_origin + nbNodes4['n2']
    for i in range(nbArcs4['k23']):
        origin = randrange(deb_origin,deb_destination)
        destination = randrange(deb_destination,deb_destination + nbNodes4['n3'])
        nodes[origin].succ.append(nodes[destination].name)
        nodes[destination].pred.append(nodes[origin].name)

    #ajout des arcs supplémentaires entre niveau 3 et 4
    deb_origin += nbNodes4['n2']
    deb_destination = deb_origin + nbNodes4['n3']
    for i in range(nbArcs4['k34']):
        origin = randrange(deb_origin,deb_destination)
        destination = randrange(deb_destination,deb_destination + nbNodes4['n4'])
        nodes[origin].succ.append(nodes[destination].name)
        nodes[destination].pred.append(nodes[origin].name)

    #ajout des arcs supplémentaires entre niveau 1 et 3
    deb_origin = 1
    deb_destination = deb_origin + nbNodes4['n1'] + nbNodes4['n2']
    for i in range(nbArcs4['k13']):
        origin = randrange(deb_origin,deb_origin + nbNodes4['n1'])
        destination = randrange(deb_destination,deb_destination + nbNodes4['n3'])
        nodes[origin].succ.append(nodes[destination].name)
        nodes[destination].pred.append(nodes[origin].name)

    #ajout des arcs supplémentaires entre niveau 2 et 4
    deb_origin += nbNodes4['n1']
    deb_destination += nbNodes4['n3']
    for i in range(nbArcs4['k24']):
        origin = randrange(deb_origin,deb_origin + nbNodes4['n2'])
        destination = randrange(deb_destination,deb_destination + nbNodes4['n4'])
        nodes[origin].succ.append(nodes[destination].name)
        nodes[destination].pred.append(nodes[origin].name)

    #ajout des arcs supplémentaires entre niveau 1 et 4
    deb_origin = 1
    deb_destination = deb_origin + nbNodes4['n1'] + nbNodes4['n2'] + nbNodes4['n3']
    for i in range(nbArcs4['k14']):
        origin = randrange(deb_origin,deb_origin + nbNodes4['n1'])
        destination = randrange(deb_destination,deb_destination + nbNodes4['n4'])
        nodes[origin].succ.append(nodes[destination].name)
        nodes[destination].pred.append(nodes[origin].name)

    #ajout des arcs supplémentaires k_
    deb = 3 #DET et PHY n'ont pas d'autres prédécesseurs
    fin = deb + sum(nbNodes4.values()) - 3 #on retire RES de la somme
    i = 0
    while i < nbArcs4['k_']:
        origin = randrange(deb,fin)
        destination = randrange(deb,fin)
        if origin > destination:
            nodes[origin].succ.append(nodes[destination].name)
            nodes[destination].pred.append(nodes[origin].name)
            i += 1

    #ajout des arcs supplémentaires loops
    deb = 3
    fin = deb + sum(nbNodes4.values()) - 4 #pas de boucle sur les noeuds fixés
    for i in range(nbArcs4['loops']):
        origin = randrange(deb,fin)
        nodes[origin].succ.append(nodes[origin].name)
        nodes[origin].pred.append(nodes[origin].name)

    #attribue un succésseur (parmi les rangs supérieurs) à chaque noeuds du rang1
    i_deb = 1
    i_fin = i_deb + nbNodes4['n1']
    deb_dest = i_fin
    fin_dest = i_fin + nbNodes4['n2'] + nbNodes4['n3'] + nbNodes4['n4'] + 1 -2 #on ajoute LOS
    for i in range(i_deb, i_fin):
        dest = randrange(deb_dest,fin_dest)
        nodes[i].succ.append(nodes[dest].name)
        nodes[dest].pred.append(nodes[i].name)

    """#élimine les doublons parmi les succ
    for i in range(sum(nbNodes4.values()) + 3):
        for j in range(len(nodes[i].succ)):
            if nodes[i].succ[j] not in nomsNoeudsFixes:
                nodes[i].succ[j] = int(nodes[i].succ[j])
        nodes[i].succ.sort()
        nodes[i].succ = set(nodes[i].succ)

    #élimine les doublons parmi les pred
    for i in range(sum(nbNodes4.values()) + 3):
        for j in range(len(nodes[i].pred) - 1):
            if nodes[i].pred[j] not in nomsNoeudsFixes:
                nodes[i].pred[j] = int(nodes[i].pred[j])
        nodes[i].pred.sort()
        nodes[i].pred = set(nodes[i].pred)"""

    return nodes


def generate_5(nbNodes5,nbArcs5):
    pass


def fichier_4(n,nodes,nbNodes4,nbArcs4): #intègre dans le fichier les noeuds, par niveau, avec leur nb de préd et leur nb de succ
    #enlève les doublons
    for i in range(n + 3):
        nodes[i].succ = set(nodes[i].succ)
        nodes[i].pred = set(nodes[i].pred)
        nodes[i].succ = list(nodes[i].succ)
        nodes[i].pred = list(nodes[i].pred)

    res = open('resultats.txt','w')

    nbNodes4['n1'] -= 2

    res.write("Nombre de sommets par niveau : " + str(nbNodes4) + '\n')
    res.write("\nNombres d'arcs : " + str(nbArcs4) + '\n')

    nbNodes4['n1'] += 2

    res.write("\nRacine\n") #FIX

    res.write("Noeud " + str(nodes[0].name) + " : d+ = " + str(len(nodes[0].succ)) + " d- = " + str(len(nodes[0].pred)) + ' / succ : ' + str(set(nodes[0].succ)) + ' pred : ' + str(set(nodes[0].pred)) + '\n')

    res.write("\nHors niveaux\n") #LOS et RES

    for i in range(n + 3,n + 5):
        res.write("Noeud " + str(nodes[i].name) + " : d+ = " + str(len(nodes[i].succ)) + " d- = " + str(len(nodes[i].pred)) + ' / succ : ' + str(nodes[i].succ) + ' pred : ' + str(nodes[i].pred) + '\n')

    res.write("\nNiveau 1\n")

    i_deb = 1
    for i in range(i_deb,nbNodes4['n1'] + i_deb):
        res.write("Noeud " + str(nodes[i].name) + " : d+ = " + str(len(nodes[i].succ)) + " d- = " + str(len(nodes[i].pred)) + ' / succ : ' + str(nodes[i].succ) + ' pred : ' + str(nodes[i].pred) + '\n')

    res.write("\nNiveau 2\n")

    i_deb += nbNodes4['n1']
    for i in range(i_deb,nbNodes4['n2'] + i_deb):
        res.write("Noeud " + str(nodes[i].name) + " : d+ = " + str(len(nodes[i].succ)) + " d- = " + str(len(nodes[i].pred)) + ' / succ : ' + str(nodes[i].succ) + ' pred : ' + str(nodes[i].pred) + '\n')

    res.write("\nNiveau 3\n")

    i_deb += nbNodes4['n2']
    for i in range(i_deb,nbNodes4['n3'] + i_deb):
        res.write("Noeud " + str(nodes[i].name) + " : d+ = " + str(len(nodes[i].succ)) + " d- = " + str(len(nodes[i].pred)) + ' / succ : ' + str(nodes[i].succ) + ' pred : ' + str(nodes[i].pred) + '\n')

    res.write("\nNiveau 4\n")

    i_deb += nbNodes4['n3']
    for i in range(i_deb,nbNodes4['n4'] + i_deb):
        res.write("Noeud " + str(nodes[i].name) + " : d+ = " + str(len(nodes[i].succ)) + " d- = " + str(len(nodes[i].pred)) + ' / succ : ' + str(nodes[i].succ) + ' pred : ' + str(nodes[i].pred) + '\n')

    res.close()


print("Bienvenue à vous dans notre super générateur de graphes d'écosystèmes !\n")

nbEsp = input("Veuillez entrer le nombre d'éspèces (entre 12 et 34) : ")
nbNiv = input("Veuillez entrer le nombre de niveaux trophiques (4) : ")

while ((int(nbEsp) < 12) or (int(nbEsp) > 34) or (int(nbNiv) != 4)):
    nbEsp = input("Veuillez entrer le nombre d'éspèces (entre 12 et 34) : ")
    nbNiv = input("Veuillez entrer le nombre de niveaux trophiques (4) : ")

generate(int(nbEsp),int(nbNiv))

for i in range(int(nbEsp) + 5):
    graphe.add_node(nodes[i].name, level=nodes[i].level)

for i in range(int(nbEsp) + 5):
    for j in range(len(nodes[i].succ)):
        graphe.add_edge(nodes[i].name,nodes[i].succ[j])



print('\n')
fichier = open('resultats.txt', 'r')
contenu = fichier.read()
print(contenu)
fichier.close()


pos = nx.multipartite_layout(graphe, subset_key='level', align='horizontal')
nx.draw_networkx_nodes(graphe, pos, node_color = 'orange', node_size = 600)
nx.draw_networkx_labels(graphe, pos)
nx.draw_networkx_edges(graphe, pos, edgelist = graphe.edges(), arrows = True)
plt.show()



