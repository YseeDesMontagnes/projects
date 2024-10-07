SRC_DIR := src
ann := ./$(SRC_DIR)/annonces
ges := ./$(SRC_DIR)/gestion
gra := ./$(SRC_DIR)/graphes
per := ./$(SRC_DIR)/personnes
ihm := ./$(SRC_DIR)/ihm
res := ./$(SRC_DIR)/reseau
sor := ./$(SRC_DIR)/sorties
OUT_DIR := classes

JC := javac
OPT := -classpath ./$(OUT_DIR) -sourcepath ./$(SRC_DIR) -d ./$(OUT_DIR)

annonce :
	$(JC) $(OPT) $(ann)/Annonce.java

annonces :
	make annonce

loyer :
	$(JC) $(OPT) $(ges)/Loyer.java

tableauPaiements :
	$(JC) $(OPT) $(ges)/TableauPaiements.java

tache :
	$(JC) $(OPT) $(ges)/Tache.java

gestion :
	make loyer tableauPaiements tache

algorithmeFourmis :
	$(JC) $(OPT) $(gra)/AlgorithmeFourmis.java

dijkstra :
	$(JC) $(OPT) $(gra)/Dijkstra.java

graphe :
	$(JC) $(OPT) $(gra)/Graphe.java

noeud :
	$(JC) $(OPT) $(gra)/Noeud.java

noeudAvecDistance :
	$(JC) $(OPT) $(gra)/NoeudAvecDistance.java

sortie :
	$(JC) $(OPT) $(gra)/Sortie.java

test :
	$(JC) $(OPT) $(gra)/Test.java

graphes :
	make algorithmeFourmis dijkstra graphe noeud noeudAvecDistance sortie test

menuColocataire :
	$(JC) $(OPT) $(ihm)/Menu_colocataire.java

menuProprio :
	$(JC) $(OPT) $(ihm)/Menu_proprio.java

menus :
	$(JC) $(OPT) $(ihm)/Menus.java

methodesMenus :
	$(JC) $(OPT) $(ihm)/Methodes_menus.java

ihm :
	make methodesMenus menus menuColocataire menuProprio

colocataire :
	$(JC) $(OPT) $(per)/Colocataire.java

personne :
	$(JC) $(OPT) $(per)/Personne.java

proprietaire :
	$(JC) $(OPT) $(per)/Proprietaire.java

personnes :
	make personne colocataire proprietaire

Accepter_clients :
	$(JC) $(OPT) $(res)/Accepter_clients.java

Client :
	$(JC) $(OPT) $(res)/Client.java

EnvoyerMessageClient :
	$(JC) $(OPT) $(res)/EnvoyerMessageClient.java

Serveur :
	$(JC) $(OPT) $(res)/Serveur.java

TransmettreMessageServeur :
	$(JC) $(OPT) $(res)/TransmettreMessageServeur.java

reseau :
	make Accepter_clients TransmettreMessageServeur EnvoyerMessageClient Client Serveur

Bars :
	$(JC) $(OPT) $(sor)/Bars.java

Sorties :
	$(JC) $(OPT) $(sor)/Sorties.java

sorties :
	make Sorties Bars

all :
	make annonces gestion graphes ihm personnes reseau sorties

main :
	make menus

lancerApp :
	java ./$(OUT_DIR)/ihm/Menus

clean :
	rm -r ./$(OUT_DIR)/*