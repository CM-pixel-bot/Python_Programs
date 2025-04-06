import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler


df = pd.read_csv("3Salary_Data.csv")
print("Original Data:\n", df)


normalizer = Normalizer()
normalized_data = normalizer.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
print("\nNormalized Data:\n", normalized_df)


scaler = MinMaxScaler()
minmax_data = scaler.fit_transform(df)
minmax_df = pd.DataFrame(minmax_data, columns=df.columns)
print("\nMin-Max Scaled Data:\n", minmax_df)

OUTPUT:
Original Data:
   YearsExperience  Salary
0              1.1   39343
1              1.3   46205
2              1.5   37731

Normalized Data:
   YearsExperience    Salary
0         2.796157e-05  1.000000
1         2.813790e-05  1.000000
2         3.976949e-05  1.000000

Min-Max Scaled Data:
   YearsExperience    Salary
0         0.0          0.304948
1         0.5          1.000000
2         1.0          0.000000
