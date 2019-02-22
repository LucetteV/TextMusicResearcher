def txt_to_csv(file_txt):
# on ouvre le fichier.txt 'Internationale' en mode lecture qu'on stocke dans une variable 'in_f'
    import csv
    with open(file_txt, mode='r') as in_f:
    # avec la méthode .strip() on retourne une copie de la chaîne de caractère moins le
    # paramètre passé en méthode. Dans le cas présent : suppression des retours chariots
    # pour un remplacement par une virgule = séparateur de base du fichier csv
    # dans la chaîne de caractère on dégage ce qu'on a mis en paramètre de la méthode .strip()
        splited = (line.splitlines() for line in in_f)
    # la variable 'lines' stocke chaque 'line' qui a été stripped
    # pour chaque 'line' strippée elle est stockée dans la variable 'lines'
        lines = (line for line in splited if line)
        with open(file_txt.replace('.txt', '.csv'), mode='w') as out_f:
            writer = csv.writer(out_f)
            writer.writerows(lines)
    return print("votre fichier a été converti en csv")

txt_to_csv('ChantduDépart.txt')
