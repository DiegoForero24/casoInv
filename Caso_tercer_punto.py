import openpyxl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_excel('C:/Users/User/Desktop/ejemplo_td1/clase_3/customer_data.xlsx')
#genero-satisfaccion
genero_segmentados = df[df['gender'] == 'Male']

print(genero_segmentados)

#region-frecuencia de compra
#estado de lealtad-monto de compra