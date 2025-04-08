import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('4laptops.csv')


print(data.head())  # Preview the first few rows of the DataFrame


plt.figure(figsize=(10, 6))
plt.boxplot(data['Price'])
plt.title('Box Plot of Laptop Prices (Matplotlib)')
plt.ylabel('Price')
plt.grid(axis='y')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x=data['Price'])
plt.title('Box Plot of Laptop Prices (Seaborn)')
plt.xlabel('Price')
plt.grid(axis='x')
plt.show()

OUTPUT:
Q1 = 40500  
Q3 = 52750  
IQR = 12250  
Lower Bound = 22125  
Upper Bound = 71125  
Outliers = [100000]
