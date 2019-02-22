## nous importons le package sqlite3
import sqlite3

## dans une variable connexion nous stockons l'objet représentant la database grâce à la méthode .connect()
connexion = sqlite3.connect("collectionTMR.sq3")

## dans une variable curseur, nous appelons la variable connexion à laquelle nous assignons la methode .cursor()
curseur = connexion.cursor()

# creation d'une table
## à l'aide de la variable curseur sur laquelle nous appliquons la méthode .execute() et qui comprend la condition de création de table 'if not exists'
## et à laquelle on donne un id (qui sera unique), un parent, un titre, un auteur, une date de création, et un fichier qui comprendra le texte
curseur.execute("CREATE TABLE IF NOT EXISTS collectionTMR (id TEXT, parent TEXT, titre TEXT, auteur TEXT, date_creation INTEGER, fichier TEXT)")

# ajout de données à la base
## nous ajoutons à la base de données la table ainsi créée
curseur.execute("INSERT INTO collectionTMR(id) VALUES('collection_initiale')")
## et à la collection initiale désormais enrichie avec pour valeurs les informations qu'elle contient
curseur.execute("INSERT INTO collectionTMR(id, parent, titre, auteur, date_creation, fichier) VALUES('revolution','collection_initiale', 'La Marseillaise', 'Rouget de l'Isle', '1792')")

# valide l'enregistrement dans la base
## et sauvegarde les changements opérés dans la base de données
connexion.commit()

# fermer la base
## (jai lu dans la doc que c'est à faire que si on est sûr d'en avoir terminer avec)
connexion.close()
