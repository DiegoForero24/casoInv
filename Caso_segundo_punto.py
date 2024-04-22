import openpyxl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_excel('C:/Users/User/Desktop/ejemplo_td1/clase_3/customer_data.xlsx')
x= df['purchase_amount']
y= df['purchase_amount']
plt.plot(x, y)  # Plot the chart
plt.show() 
print("////////")