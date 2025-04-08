import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df2 = pd.read_csv("4laptop.csv")


plt.boxplot(df2['Screen_size_inches'], notch=True, vert=False, showmeans=True, sym="*", patch_artist=True, widths=0.1)
plt.xlabel('Screen Size (inches)')
plt.ylabel('Laptops')
plt.title('Boxplot of Screen Sizes')
plt.show()


plt.boxplot(df2['Weight_kg'])
plt.xlabel('Laptops')
plt.ylabel('Weight (kg)')
plt.title('Boxplot of Laptop Weights')
plt.show()


sns.boxplot(x=df2['Weight_kg'])
plt.title('Seaborn Boxplot of Laptop Weights')
plt.show()


sns.boxplot(x=df2['Weight_kg'], y=df2['RAM'])
plt.title('Weight vs RAM')
plt.show()

OUTPUT:
