import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


df = pd.read_csv('laptops.csv')


ohe = OneHotEncoder()
os_encoded = ohe.fit_transform(df[['Operating System']]).toarray()
os_df = pd.DataFrame(os_encoded, columns=ohe.get_feature_names_out(['Operating System']))


le = LabelEncoder()
df['Storage_Label'] = le.fit_transform(df['Storage'])


final_df = pd.concat([df, os_df], axis=1)


print(final_df[['Operating System', 'Storage', 'Storage_Label'] + list(os_df.columns)])



