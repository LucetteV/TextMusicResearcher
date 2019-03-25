#j'ouvre le fichier txt.
with open ("..//Collection_initiale/Chants_contre/Triomphe_Anarchie.txt", 'r') as f:
    #je crée le fichier xml de sortie.
    with open('Triomphe_Anarchie.xml', 'w') as new_xml:
        #je rédige le préambule du cml
        new_xml.write('<?xml version="1.0" encoding="UTF-8"?>' '\n')
        #j'ajoute les déclarations propres à TEI pour que le fichier soit valide.
        new_xml.write('<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>' '\n'
                '<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>' '\n'
                '<TEI xmlns="http://www.tei-c.org/ns/1.0">' '\n'
                      '<body>''\n')
        #pour chaque ligne du fichier texte j'ajoute la ligne entre balise au document xml
        for line in f:
            new_xml.write('<l>'+line+'</l>''\n')
        #je referme les balises <body> et <TEI>.
        new_xml.write('</body>''\n''</TEI>')