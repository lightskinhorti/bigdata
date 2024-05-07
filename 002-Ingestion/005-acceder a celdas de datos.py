import pandas as pd

archivo = pd.read_excel("xls/clientes.ods",engine="odf")
celda = archivo.iloc[0,0]
print(celda)