import openpyxl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_excel('C:/Users/User/Desktop/ejemplo_td1/clase_3/customer_data.xlsx')
variables_seleccionadas = ['age', 'income', 'purchase_amount', 'satisfaction_score']
datos_seleccionados = df[variables_seleccionadas]

matriz_correlacion = datos_seleccionados.corr()
print(matriz_correlacion)
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor de Correlación')
plt.show()


variables_dummy = pd.get_dummies(df['loyalty_status'], prefix='loyalty_status')

df_con_dummy = pd.concat([df['satisfaction_score'], variables_dummy], axis=1)


matriz_correlacion2 = df_con_dummy.corr()

print(matriz_correlacion2)
