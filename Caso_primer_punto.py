import openpyxl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_excel('C:/Users/User/Desktop/ejemplo_td1/clase_3/customer_data.xlsx')
#Edad
print("////////")
media_edad = df['age'].mean()
print("Media de la columna 'edad':", media_edad)
sns.barplot(x=df['age'].value_counts().index, y=df['age'].value_counts(), color='red')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()
print("////////")
#Genero
conteo_genero= df['gender'].value_counts()
print("Genero:", conteo_genero)
moda_genero = df['gender'].mode()[0]
print("Moda de la columna genero es:", moda_genero)
plt.figure(figsize=(8, 6))
df['gender'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Diagrama de Torta para distribución de Columna genero', fontsize=16)
plt.ylabel('')  
plt.show()
print("////////")
#Ingresos
media_ingresos = df['income'].mean()
print("Media de la columna 'ingresos':", media_ingresos)
Max_ingresos = df['income'].max() 
print("El ingreso minimo de los clientes es:", Max_ingresos)
Min_ingresos= df['income'].min()
print("El ingreso maximo de los clientes es:", Min_ingresos)
Rango_ingresos= df['income'].max() - df['income'].min()
print("El rango de la columna Ingresos es:", Rango_ingresos)
desviacion_ingresos = df['income'].std()
print(" Desviacion estandar es:", desviacion_ingresos)

x = df['income']
y = df['income']
 
plt.plot(x, y)  # Plot the chart
plt.show()  
print("////////")
#Educacion
conteo_educacion= df['education'].value_counts()
print(":", conteo_educacion)
moda_educacion = df['education'].mode()[0]
print("Moda de la columna educacion es:", moda_educacion)
sns.barplot(x=df['education'].value_counts().index, y=df['education'].value_counts(), color='red')
plt.title('Distribución de Educacion')
plt.xlabel('Education')
plt.ylabel('Frecuencia')
plt.show()
print("////////")
#Region
conteo_region= df['region'].value_counts()
print("Region:", conteo_region)
moda_region = df['region'].mode()[0]
print("Moda de la columna region es:", moda_region)
plt.figure(figsize=(8, 6))
df['region'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Diagrama de Torta para distribución de Columna region', fontsize=16)
plt.ylabel('')  
plt.show()
print("////////")
#loyalty_status
conteo_membresia= df['loyalty_status'].value_counts()
print("Membresia:", conteo_membresia)
moda_membresia = df['loyalty_status'].mode()[0]
print("Moda de la columna membresia es:", moda_membresia)
sns.barplot(x=df['loyalty_status'].value_counts().index, y=df['loyalty_status'].value_counts(), color='red')
plt.title('Distribución de membresia')
plt.xlabel('loyalty_status')
plt.ylabel('Frecuencia')
plt.show()
print("////////")
#Frecuencia de la compra
conteo_frecuencia= df['purchase_frequency'].value_counts()
print("Frecuencia:", conteo_frecuencia)
moda_frecuencia = df['purchase_frequency'].mode()[0]
print("Moda de la columna frecuencia es:", moda_frecuencia)
plt.figure(figsize=(8, 6))
df['purchase_frequency'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Diagrama de Torta para distribución de Columna frecuencia', fontsize=16)
plt.ylabel('')  
plt.show()
print("////////")
#Monto de la compra
media_monto = df['purchase_amount'].mean()
print("Media de la columna 'Monto de la compra':", media_monto)
Max_monto = df['purchase_amount'].max() 
print("El monto maximo de los clientes es:", Max_monto)
Min_monto= df['purchase_amount'].min()
print("El monto minimo de los clientes es:", Min_monto)
Rango_monto= df['purchase_amount'].max() - df['purchase_amount'].min()
print("El rango de la columna monto es:", Rango_monto)
desviacion_monto = df['purchase_amount'].std()
print("Desviación estándar:", desviacion_monto)
print("////////")
#Categoria del producto
conteo_producto= df['product_category'].value_counts()
print("Categoria:", conteo_producto)
moda_producto = df['product_category'].mode()[0]
print("Moda de la columna frecuencia es:", moda_producto)
sns.barplot(x=df['product_category'].value_counts().index, y=df['product_category'].value_counts(), color='red')
plt.title('Distribución de producto')
plt.xlabel('purchase_frequency')
plt.ylabel('Frecuencia')
plt.show()
print("////////")
#Uso de promocion
moda_promocion = df['promotion_usage'].mode()[0]
print("Moda de la columna Uso de la promocion es:", moda_promocion)
plt.figure(figsize=(8, 6))
df['promotion_usage'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Diagrama de Torta para distribución de Columna promocion', fontsize=16)
plt.ylabel('')  
plt.show()
print("////////")
#Satisfacion
moda_satisfaccion = df['satisfaction_score'].mode()[0]
print("Moda de la columna satisfaccion es:", moda_satisfaccion)
media_satisfaccion = df['satisfaction_score'].mean()
print("Media de la columna satisfaccion es:", media_satisfaccion)
sns.displot(df['satisfaction_score'], kde = False, color ='red', bins = 30) 
plt.show()
