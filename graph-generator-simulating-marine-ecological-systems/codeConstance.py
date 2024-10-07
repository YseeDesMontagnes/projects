from random import randrange
from random import randint
import random

#declaration de certaines variables
nbArcs4 = {}
nbArcs4['k12'] = 0
nbArcs4['k23'] = 0
nbArcs4['k34'] = 0
nbArcs4['k13'] = -1
nbArcs4['k24'] = -1
nbArcs4['k14'] = -1
nbArcs4['loops'] = -1
nbArcs4['k_'] = -1


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

print('\n')
fichier = open('resultats.txt', 'r')
contenu = fichier.read()
print(contenu)
fichier.close()