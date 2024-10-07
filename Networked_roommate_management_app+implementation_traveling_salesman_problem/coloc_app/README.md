# Bienvenue dans le guide d'utilisateur de notre application Coloc'APP !

Les fichiers de code source sont rangés dans le dossier src et les fichiers compilés dans le dossier classes.

## Configuration pour la partie réseau :
1. Tout le monde doit être connecté sur le même réseau ;
2. Sur chaque PC qui n'hébergera pas le serveur, veuillez entrer dans la classe _Client_ (dossier _reseau_) l'adresse IP de l'hôte dans le champ IP_SERV.

## Lancement depuis votre IDE préféré :
 1. Si vous n'êtes pas hôte, rendez-vous à l'étape 2., sinon, lancez le main de la classe _Serveur_ (dossier _reseau_) ;
 2. Chaque utilisateur peut lancer le main de la classe _Menus_ (dossier _ihm_) qui est notre application ;
 3. 4 profils sont enregistrés, rendez-vous dans la section Profils pour avoir les informations de connexion ;
 4. N'oubliez pas d'éteindre le serveur après la fermeture des applications.

## Lancement depuis un terminal linux :
 1. Dans le dossier Coloc'APP, lancez la commande `make all` ;
 2. Déplacez-vous vers le dossier classes ;
 3. Si vous n'êtes pas hôte, rendez-vous à l'étape 2., sinon, lancez le main de la classe _Serveur_ (commande : `java reseau.Serveur`) ;
 4. Chaque utilisateur peut lancer le main de la classe _Menus_ (commande : `java ihm.Menus`) qui est notre application ;
 5. 4 profils sont enregistrés, rendez-vous dans la section Profils pour avoir les informations de connexion ;
 6. N'oubliez pas d'éteindre le serveur après la fermeture des applications.

## Profils :
4 profils sont entrés dans le programme, chaque profil dispose d'un identifiant (_PrénomNom_) et d'un mot de passe (_PrénomNom123_).

Voici ces 4 profils :

#### Propiétaire :
 1. Prénom : "Jean", Nom : "Michel"
#### Colocataires :
 1. Prénom : "Paul", Nom : "Méhaud"
 2. Prénom : "Kenza", Nom : "Bennani"
 3. Prénom : "Ines", Nom : "Silhadi"