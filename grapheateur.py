from random import randrange, randint
import networkx as nx
import matplotlib.pyplot as plt
import random

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


print("Bienvenue dans le Grapheateur (générateur de graphes) !")
print()
print("Nous vous proposons de choisir entre un mode plus aléatoire, mais moins représentatif des ecosystèmes et un mode moins aléatoire, mais plus représentatif des ecosystèmes.")
print()
choix = int(input("Tapez 1 pour simuler un graphe pouvant correspondre à un réseau trophique sans choisir la densité entre chaque niveau ou 2 pour simuler un graphe pouvant correspondre à un réseau trophique d'un écosystème marin en choississant la densité : "))
i=0
while ((int(choix) < 1) or (int(choix) > 2)):
    choix = int(input("Tapez 1 pour simuler un graphe pouvant correspondre à un réseau trophique sans choisir la densité entre chaque niveau ou 2 pour simuler un graphe pouvant correspondre à un réseau trophique d'un écosystème marin en choississant la densité : "))

print()

if choix == 2:
    #ATTENTION cette fonction doit être utilisée avec un nombre de sommet compris en 12 et 34
    def levels(n):
        #revoie une liste dont le nième chiffre correspond au nombre d'espèces du nième+1 niveau trophique

        liste=[1]*4
        p=0
        liste[2]=2
        liste[0]=-1
        #ces 2 affectations premettent de faire la boucle au moins une fois
        while liste[1]<liste[2] or liste[0]<0:
            #la 1ère condition assure que les nombre de sommet est décroissant du niveau 2 au niveau 4 et la 2ème assure qu'il n'y ait pas un nombre négatif d'espèces au niveau 1, en revanche il peut y en avoir 0 car en dehors de la boucle on en ajoutera 2 correspondant à DET et PHY
            a=randint(1,6)
            if a==1 :
                liste[3]=2
            if a==2 :
                liste[3]=4
            if a>2:
                liste[3]=3

            #le bloc précédent permet d'affecter un nombre de sommet compris entre 2 et 4 au niveau trophique 4 avec une probabilité 3 fois plus grande d'affecter le nombre 3 (on s'est inpiré du tableau de données)

            b=randint(1,10)
            if n<17 :
                if b<6:
                    liste[2]=4
                else :
                    if b>9:
                        liste[2]=5
                    else:
                        liste[2]=6
            if n>24 :
                if b<6:
                    liste[2]=6
                else :
                    if b>9:
                        liste[2]=5
                    else:
                        liste[2]=4
            if 17<=n<25:
                liste[2]=randint(4,7)


            #le bloc précédent permet d'affecter un nombre compris entre 4 et 6 au sommet 3 avec des probalités différentes d'obtenir chacunes de ces 3 valeurs pour permettre d'avoir plus de chance d'obtenir 5 ou 6 lorsque n est grand et moins de chance lorsque n est petit


            liste[1]=randint(int(n//3),int(n//2)+1)
            #cette instruction permet d'affecter un nombre de sommets compris entre la partie entière du tiers de n et la partie entière de la moitié de n + 1 car on a remarqué grâce au tableau que les réseaux trophiques étudiés respectaient cette condition
            liste[0]=n-liste[2]-liste[3]-liste[1]
            #affecte au niveau 1 le nombre d'espèces restantes
        liste[0]=liste[0]+2
        #rajoute au niveau 1 deux espèces qui sont les espèces phytoplancton et detritut toujours situees au niveau 1 permet de voir le nombre de fois que le programme a effectuer la boucle avnt de trouver une liste respectant les ddeux conditions principales


        return liste

    def calcul_min_densite(nb_sommets_nivx):
        #cette fonction retourne la densité minimum entre le niveau n et son niveau suivant le niveau x
        return(1/nb_sommets_nivx)
        #l'utilisateur choisi le nombre d'especes
    nb_especes = int(input("Choississez le nombre d'espèce du réseau trophique à modéliser, ce nombre doit être compris entre 12 et 34 : "))
    while ((nb_especes < 12) or (nb_especes > 34)):
        nb_especes = int(input("Choississez le nombre d'espèce du réseau trophique à modéliser, ce nombre doit être compris entre 12 et 34 : "))

    x=levels(nb_especes)
        #on creer une liste vide que l'on remplira avec la densité entre chaque niveau saisie par l'utilisateur
    liste_dens=[]
    for i in range (0,3):
        a=calcul_min_densite(x[i])
        print("Entrez la densité entre le niveau", i+1,"et le niveau", i+2,"superieure ou egale à ",a,"et strictement inferieure à 1 : ")
        dens = float(input())
        #on verifie la saisie de l'utilisateur, malheureusement il n'y a pas de repeat until en python
        while ((dens < a) or (dens >= 1)):
            print("Entrez la densité entre le niveau", i+1,"et le niveau", i+2,"superieure ou egale à ",a,"et strictement inferieure à 1 : ")
            dens = float(input())

        liste_dens.append(dens)
    print("\nVoici un résumé des densités :", liste_dens)


    #on va determiner le nombre de sommets entre 2 niveaux en respectant la densité saisie par l'utilisateur
    nbArcs4['k12'] = int(liste_dens[0]*x[0]*x[1])+1
    nbArcs4['k23'] = int(liste_dens[1]*x[1]*x[2])+1
    nbArcs4['k34'] = int(liste_dens[2]*x[2]*x[3])+1

    #on choisie "au hasard" le nombre de sommets entre 2 niveaux non côte à côte grâce a un tirage au hasard dans une repartition gaussienne qui nous a été inspirée par le tableau de données
    while nbArcs4['k13']<0 :
        nbArcs4['k13'] = int(random.gauss(3,(x[0]*x[2])/3))
    while nbArcs4['k24']<0 :
        nbArcs4['k24'] = int(random.gauss(3,(x[1]*x[3])/3))
    while nbArcs4['k14']<0 :
        nbArcs4['k14'] = int(random.gauss(0,1/3))
    #tirage des boucles et des arcs en sens inverse
    while nbArcs4['loops']<0 :
        nbArcs4['loops'] = int(random.gauss(0,1/2))
    while nbArcs4['k_']<0 :
        nbArcs4['k_'] = int(random.gauss(8,5))






    #on va maintenant creer une matrice de taille nb_especes+3*nb_especes+3 qui representera la matrice d'adjacence du graphe, elle contient nb_especes espèces (nb_especes est entré par l'utilisateur) ainsi que les espèces PHY, DET et FIX
    mat_graphe=[[0 for i in range(0,nb_especes+3)]for j in range(0,nb_especes+3)]
    #le sommet FIX est représenté par l'indice 0 de la matrice, on créer l'arc partant de FIX et allant a PHY qui est représenté par l'indice 1 de la matrice
    mat_graphe[0][1]=1
    #precisions : le sommet DET est representer par l'indice 2 et il appartient au niveau 1,il ne peut avoir que PHY comme prédécesseur
    mat_graphe[1][2]=1
    #on passe a la creation des arcs
    #on va créer les arcs entre le sommet 1 et le sommet 2 (donc k12 arcs)
    for i in range(x[0]+1,x[0]+x[1]+1):

        a=randint(1,x[0])
        mat_graphe[a][i]=1
    c=nbArcs4['k12']-x[1]
    i=0
    while i!=c:
        e=randint(1,x[0])
        f=randint(x[0]+1,x[0]+x[1])

        if mat_graphe[e][f]==0 :
            i=i+1
            mat_graphe[e][f]=1
    #on va creer les arcs entre le niveau 2 et le niveau 3 (donc k23 arcs)
    for i in range(x[1]+x[0]+1,x[0]+x[1]+x[2]+1):

        a=randint(x[0]+1,x[0]+x[1])
        mat_graphe[a][i]=1
    c=nbArcs4['k23']-x[2]
    i=0
    while i!=c:
        e=randint(x[0]+1,x[0]+x[1])
        f=randint(x[1]+x[0]+1,x[0]+x[1]+x[2])

        if mat_graphe[e][f]==0 :
            i=i+1
            mat_graphe[e][f]=1
    #on va creer les arcs entre le niveau 3 et le niveau 4 (donc k34 arcs)
    for i in range(x[0]+x[1]+x[2]+1,x[0]+x[1]+x[2]+x[3]+1):

        a=randint(x[0]+x[1]+1,x[0]+x[1]+x[2])
        mat_graphe[a][i]=1
    c=nbArcs4['k34']-x[3]
    i=0
    while i!=c:
        e=randint(x[0]+x[1]+1,x[0]+x[1]+x[2])
        f=randint(x[0]+x[1]+x[2]+1,x[0]+x[1]+x[2]+x[3])

        if mat_graphe[e][f]==0 :
            i=i+1
            mat_graphe[e][f]=1
    #on va creer les arcs entre le niveau 1 et le niveau 3 (donc k13 arcs)
    i=0
    while i!=nbArcs4['k13']:
        e=randint(1,x[0])
        f=randint(x[0]+x[1]+1,x[0]+x[1]+x[2])

        if mat_graphe[e][f]==0 :
            i=i+1
            mat_graphe[e][f]=1
    #on va creer les arcs entre le niveau 2 et le niveau 4 (donc k24 arcs)
    i=0
    while i!=nbArcs4['k24']:
        f=randint(x[0]+x[1]+x[2]+1,x[0]+x[1]+x[2]+x[3])
        e=randint(x[0]+1,x[0]+x[1])

        if mat_graphe[e][f]==0 :
            i=i+1
            mat_graphe[e][f]=1
    #on va creer les arcs entre le niveau 1 et le niveau 4 (donc k13 arcs)
    i=0
    while i!=nbArcs4['k14']:
        f=randint(x[0]+x[1]+x[2],x[0]+x[1]+x[2]+x[3])
        e=randint(1,x[0])

        if mat_graphe[e][f]==0 :
            i=i+1
            mat_graphe[e][f]=1

    #on va creer les arcs entre le niveau entre inter-niveaux ou partant d'un niveau superieur et allant vers un niveau inferieur
    i=0
    while i!=nbArcs4['k_']:
        f=randint(4,nb_especes+2)
        e=randint(3,f-1)

        if mat_graphe[f][e]==0:
            i=i+1
            mat_graphe[f][e]=1
    #on va creer les arcs entre les boucles (nbArcs['loops'] boucles)
    i=0
    while i!=nbArcs4['loops']:
        e=randint(3,nb_especes+3)

        if mat_graphe[e][e]==0:
            i=i+1
            mat_graphe[e][e]=1


    #Ce bloc permet de verifier qu'il n'y ait pas de sommets du niveau 1 sans successeurs, cela arrive très très rarement mais au cas où ca arriverait ce bloc permet d'affecter un successeur au hasard aux sommets de niveau 1 sans successeurs
    for c in range(3,x[0]+1):
        g=0

        while((g<=nb_especes+2)and(mat_graphe[c][g]==0)):
            g=g+1

        if (g>nb_especes+2):
            succ=randint(c+1,nb_especes+2)
            mat_graphe[c][succ]=1
            print('ok')





    #on passe à la partie affichage
    nbNodes={}
    nbNodes['n1'] = x[0]
    nbNodes['n2'] = x[1]
    nbNodes['n3'] = x[2]
    nbNodes['n4'] = x[3]

    res = open('resultats.txt','w')

    print()
    res.write("Nombre de sommets par niveau : " + str(nbNodes) + "\n")
    res.write("\nNombres d'arcs : " + str(nbArcs4) + "\n")
    res.write("\nLes noeuds FIX, PHY et DET sont respectivement représentés par 0, 1 et 2.\n")
    num_prem_som_niv=0
    for i in range(0,4):
        res.write('\nNiveau ' + str(i+1) + '\n')

        for j in range(num_prem_som_niv+1,num_prem_som_niv+x[i]+1):
            d_plus=0
            succ = list()
            for k in range(0,nb_especes+3):
                if mat_graphe[j][k]==1:
                    succ.append(str(k))
                    d_plus += 1

            d_moins=0
            pred = list()
            for k in range(0,nb_especes+3):
                if mat_graphe[k][j]==1:
                    pred.append(str(k))
                    d_moins += 1

            res.write('Noeud ' + str(j) + ' : d+ = '+str(d_plus)+' d- = '+str(d_moins) + ' / succ : ' + str(succ) + ' pred : ' + str(pred) + '\n')

        num_prem_som_niv=num_prem_som_niv+x[i]

    res.close()






if choix == 1:
    graphe = nx.DiGraph()

    nomsNoeudsFixes = ['DET', 'FIX', 'RES', 'LOS', 'PHY']

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


    """def edges_5(nbNodes5):
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

        return nbArcs5"""

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

        #élimine les doublons parmi les succ
        """for i in range(sum(nbNodes4.values()) + 3):
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


    pos = nx.multipartite_layout(graphe, subset_key='level', align='horizontal')
    nx.draw_networkx_nodes(graphe, pos, node_color = 'orange', node_size = 600)
    nx.draw_networkx_labels(graphe, pos)
    nx.draw_networkx_edges(graphe, pos, edgelist = graphe.edges(), arrows = True)
    plt.show()


print('\n')
fichier = open('resultats.txt', 'r')
contenu = fichier.read()
print(contenu)
fichier.close()



