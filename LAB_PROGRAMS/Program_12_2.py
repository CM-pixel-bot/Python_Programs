import pandas as pd
data = pd.read_csv('4laptops.csv')
data 
q3 = data['Weight_kg'].quantile(0.75)
q1 = data['Weight_kg'].quantile(0.25)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = data[(data['weight_kg'] < lower_bound)| (data['Weight_kg'] > upper_bound)]
print('lower bound,upper bound and iqr values are:',lower_bound,upper_bound, iqr)
print('No.of outliers are:',outliers.shape[0])

OUTPUT:
Input:[1.0, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 3.0, 4.8]
Q1 (25th percentile): ~1.4

Q3 (75th percentile): ~2.25

IQR (Q3 - Q1): 0.85

Lower Bound: 0.175

Upper Bound: 3.575

Only one outlier: 4.8 (since it is > 3.575)
