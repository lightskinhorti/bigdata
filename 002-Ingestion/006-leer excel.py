import pandas as pd

archivo = pd.read_excel("xls/clientes.xlsx")
print(archivo)
celda = archivo.iloc[0,0]
print(celda)