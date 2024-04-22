import openpyxl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_excel('C:/Users/User/Desktop/ejemplo_td1/clase_3/customer_data.xlsx')
#genero-frecuencia de compra
#Male
print("Genero Hombre")
hombre_segmentados = df[df['gender'] == 'Male']
conteo_condicional = ((hombre_segmentados['purchase_frequency'] =='occasional')).sum()
print("Cantidad de de hombres que frecuentan a comprar de manera 'occasional'':", conteo_condicional)
conteo_condicional2 = (hombre_segmentados['purchase_frequency'] =='rare').sum()
print("Cantidad de de hombres que frecuentan a comprar de manera 'rare'':", conteo_condicional2)
conteo_condicional3 = (hombre_segmentados['purchase_frequency'] =='frequent').sum()
print("Cantidad de de hombres que frecuentan a comprar de manera 'frequent'':", conteo_condicional3)

#Female
print("Genero Mujer")
mujer_segmentados = df[df['gender'] == 'Female']
conteo_condicional4 = (mujer_segmentados['purchase_frequency'] =='occasional').sum()
print("Cantidad de mujeres que frecuentan a comprar de manera 'occasional'':", conteo_condicional4)
conteo_condicional5 = (mujer_segmentados['purchase_frequency'] =='rare').sum()
print("Cantidad de mujeres que frecuentan a comprar de manera 'rare'':", conteo_condicional5)
conteo_condicional6 = (mujer_segmentados['purchase_frequency'] =='frequent').sum()
print("Cantidad de mujeres que frecuentan a comprar de manera 'frequent'':", conteo_condicional6)
#region-frecuencia de compra
print("Region-North")
north_segmentados = df[df['region'] == 'North']
conteo_condicional7 = ((north_segmentados['purchase_frequency'] =='occasional')).sum()
print("Cantidad de personas de la region 'North' que frecuentan a comprar de manera 'occasional'':", conteo_condicional7)
conteo_condicional8 = (north_segmentados['purchase_frequency'] =='rare').sum()
print("Cantidad de personas de la region 'North' que frecuentan a comprar de manera 'rare'':", conteo_condicional8)
conteo_condicional9 = (north_segmentados['purchase_frequency'] =='frequent').sum()
print("Cantidad de personas de la region 'North' que frecuentan a comprar de manera 'frequent'':", conteo_condicional9)

print("Region-South")
south_segmentados = df[df['region'] == 'South']
conteo_condicional10 = ((south_segmentados['purchase_frequency'] =='occasional')).sum()
print("Cantidad de personas de la region 'South' que frecuentan a comprar de manera 'occasional'':", conteo_condicional10)
conteo_condicional11 = (south_segmentados['purchase_frequency'] =='rare').sum()
print("Cantidad de personas de la region 'South' que frecuentan a comprar de manera 'rare'':", conteo_condicional11)
conteo_condicional12 = (south_segmentados['purchase_frequency'] =='frequent').sum()
print("Cantidad de personas de la region 'South' que frecuentan a comprar de manera 'frequent'':", conteo_condicional12)

print("Region-West")
west_segmentados = df[df['region'] == 'West']
conteo_condicional13 = ((west_segmentados['purchase_frequency'] =='occasional')).sum()
print("Cantidad de personas de la region 'West' que frecuentan a comprar de manera 'occasional'':", conteo_condicional13)
conteo_condicional14 = (west_segmentados['purchase_frequency'] =='rare').sum()
print("Cantidad de personas de la region 'West' que frecuentan a comprar de manera 'rare'':", conteo_condicional14)
conteo_condicional15 = (west_segmentados['purchase_frequency'] =='frequent').sum()
print("Cantidad de personas de la region 'West' que frecuentan a comprar de manera 'frequent'':", conteo_condicional15)

print("Region-East")
east_segmentados = df[df['region'] == 'East']
conteo_condicional16 = ((east_segmentados['purchase_frequency'] =='occasional')).sum()
print("Cantidad de personas de la region 'East' que frecuentan a comprar de manera 'occasional'':", conteo_condicional16)
conteo_condicional17 = (east_segmentados['purchase_frequency'] =='rare').sum()
print("Cantidad de personas de la region 'West' que frecuentan a comprar de manera 'rare'':", conteo_condicional17)
conteo_condicional18 = (east_segmentados['purchase_frequency'] =='frequent').sum()
print("Cantidad de personas de la region 'West' que frecuentan a comprar de manera 'frequent'':", conteo_condicional18)
#estado de lealtad-frecuencia de la compra
print("Membresia-Gold")
gold_segmentados = df[df['loyalty_status'] == 'Gold']
conteo_condicional19 = ((gold_segmentados['purchase_frequency'] =='occasional')).sum()
print("Cantidad de personas con lealtad 'Gold' que frecuentan a comprar de manera 'occasional'':", conteo_condicional19)
conteo_condicional20 = (gold_segmentados['purchase_frequency'] =='rare').sum()
print("Cantidad de personas con la lealtad 'Gold' que frecuentan a comprar de manera 'rare'':", conteo_condicional20)
conteo_condicional21 = (gold_segmentados['purchase_frequency'] =='frequent').sum()
print("Cantidad de personas con la lealtad 'Gold' que frecuentan a comprar de manera 'frequent'':", conteo_condicional21)
print("Membresia-Silver")
silver_segmentados = df[df['loyalty_status'] == 'Silver']
conteo_condicional22 = ((silver_segmentados['purchase_frequency'] =='occasional')).sum()
print("Cantidad de personas con lealtad 'Silver' que frecuentan a comprar de manera 'occasional'':", conteo_condicional22)
conteo_condicional23 = (silver_segmentados['purchase_frequency'] =='rare').sum()
print("Cantidad de personas con la lealtad 'Silver' que frecuentan a comprar de manera 'rare'':", conteo_condicional23)
conteo_condicional24 = (silver_segmentados['purchase_frequency'] =='frequent').sum()
print("Cantidad de personas con la lealtad 'Silver' que frecuentan a comprar de manera 'frequent'':", conteo_condicional24)
print("Membresia-Regular")
regular_segmentados = df[df['loyalty_status'] == 'Regular']
conteo_condicional22 = ((regular_segmentados['purchase_frequency'] =='occasional')).sum()
print("Cantidad de personas con lealtad 'Regular' que frecuentan a comprar de manera 'occasional'':", conteo_condicional22)
conteo_condicional23 = (regular_segmentados['purchase_frequency'] =='rare').sum()
print("Cantidad de personas con la lealtad 'Regular' que frecuentan a comprar de manera 'rare'':", conteo_condicional23)
conteo_condicional24 = (regular_segmentados['purchase_frequency'] =='frequent').sum()
print("Cantidad de personas con la lealtad 'Regular' que frecuentan a comprar de manera 'frequent'':", conteo_condicional24)