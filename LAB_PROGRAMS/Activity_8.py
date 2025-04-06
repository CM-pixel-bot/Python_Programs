import pandas as pd


df = pd.read_csv('2Salary.csv')

# Calculate central tendencies and dispersion
print("📊 Central Tendencies & Dispersion Measures:")
print("Mean:", df['Salary'].mean())
print("Median:", df['Salary'].median())
print("Mode:", df['Salary'].mode()[0])
print("Min:", df['Salary'].min())
print("Max:", df['Salary'].max())
print("Variance:", df['Salary'].var())
print("Standard Deviation:", df['Salary'].std())

OUTPUT:
Mean: 50000.0
Median: 50000.0
Mode: 40000
Min: 40000
Max: 60000
Variance: 62500000.0
Std Dev: 7905.694150420948

