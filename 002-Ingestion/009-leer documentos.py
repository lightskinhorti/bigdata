from odf import text,teletype
from odf.opendocument import load

archivo = load("word/Prueba.odt")
for bloque in archivo.getElementsByType(text.P):
    print(teletype.extractText(bloque))