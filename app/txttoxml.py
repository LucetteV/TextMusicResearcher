from flask import Flask, render_template

with open("..//Collection_initiale/Chants_contre/Triomphe_Anarchie.txt") as f:
    rd = f.readlines()

with open('Triomphe_Anarchie.xml', 'w') as xml_f:
    xml_f.write('<?xml version="1.0" encoding="UTF-8"?>' '\n')
    xml_f.write('<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>' '\n'
                '<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>' '\n'
                '<TEI xmlns="http://www.tei-c.org/ns/1.0">' '\n')
    xml_f.write('<body>' '\n' '<p>''\n')

    xml_f.write('</p>''\n''</body>''\n')
    xml_f.write('</TEI>' '\n')

def index():
    return render_template('index.xml', application='text/xml')