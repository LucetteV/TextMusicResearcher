# on importe le package csv (ce module permet de lire et d'écrire des fichiers csv)
import csv
# on importe le package intertools (ce module implémente des iterations sur des blocks)
#import itertools

# on ouvre le fichier.txt 'Internationale' en mode lecture qu'on stocke dans une variable 'in_f'
with open('Internationale.txt', 'r') as in_f:
    # avec la méthode .strip() on retourne une copie de la chaîne de caractère moins le
    # paramètre passé en méthode. Dans le cas présent : suppression des retours chariots
    # pour un remplacement par une virgule = séparateur de base du fichier csv
    # dans la chaîne de caractère on dégage ce qu'on a mis en paramètre de la méthode .strip()
    splited = (line.splitlines() for line in in_f)
    # la variable 'lines' stocke chaque 'line' qui a été stripped
    # pour chaque 'line' strippée elle est stockée dans la variable 'lines'
    lines = (line for line in stripped if line)
    #
    #grouped = itertools.izip(*[lines] * 3)
    with open('Internationale.csv', 'w') as out_f:
        writer = csv.writer(out_f)
        ##writer.writerow(('title', 'author'))
        writer.writerows(lines)
