import pandas as pd


products = [
    {'Product': 'Laptop', 'Category': 'Electronics', 'Price': 50000},
    {'Product': 'Shirt', 'Category': 'Clothing', 'Price': 1500},
    {'Product': 'Book', 'Category': 'Education', 'Price': 500}
]


df = pd.DataFrame(products)

df['Discounted Price'] = df['Price'] * 0.90

print(df)

OUTPUT:
  Product    Category  Price  Discounted Price
0  Laptop  Electronics  50000           45000.0
1   Shirt     Clothing   1500            1350.0
2    Book    Education    500             450.0
