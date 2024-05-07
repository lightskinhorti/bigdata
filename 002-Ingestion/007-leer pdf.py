import PyPDF2

archivo = PyPDF2.PdfReader("pdf/prueba.pdf")
print(archivo)
paginas = len(archivo.pages)
print(paginas)

for pagina in range (0,paginas):
    actual = archivo.pages(paginas)
    print(actual.extract_text())