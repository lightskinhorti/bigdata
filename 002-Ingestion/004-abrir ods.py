import pandas as pd

archivo = pd.read_excel("xls/clientes.ods",engine="odf")
print(archivo)