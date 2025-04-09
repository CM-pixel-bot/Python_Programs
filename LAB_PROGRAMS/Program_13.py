import pandas as pd

#creating the employee_details DataFrame
employee_details = pd.DataFrame({
  'Employee ID':[101, 102, 103, 104, 105],
  'Name':['Alice','Bob','Charlie','David','Eva'],
  'Department':['HR','Engineering','Engineering','HR','Marketing']
})

employee_salaries = pd.DataFrame({
  'Employee ID':[101,102,103,104,105],
  'Salary':[50000,70000,80000,55000,60000]
})

sales_region_1 = pd.DataFRame({
  'Date':pd.date_range(start="2024-01-01',periods=5,freq='D'),
  'Region':['North','North','North','North','North'],
  'Sales':[250,300,200,400,350]
})

sales_region_2 = pd.DataFrame({
  'Date':pd.date_range(start='2024-01-01',periods=5,freq='D'),
   'Region':['South','South','South','South','SOuth'],
  'sales':[300,320,280,360,310]
})

print("Employee Details:")
print(employee_details)
print("\nEmployee Salaries:")
print(employee_salaries)
print("\nSales region 1:")
print(sales_region_1)
print("\nSales region 2:")
print(sales_region_2)

#Grouping
avg_salary_per_dept = employee_details.merge(employee_salaries,on = "EmployeeID').groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")
print(avg_salary_per_dept)

#merging
merged_data = pd.merge(employee_details,employee_salaries,on='Employee ID',how = 'inner')
print("\nMerged Employee Data:")
print(merged_data)

#joining
import pandas as pd
stock_prices = pd.DataFrame({
'Date':pd.date_range(start='2024-01-01',periods=5,freq='D'),
'Price':[150,155,152,158,160]
})
stock_prices.set_index('Date',inplace=True)

market_volume = pd.DataFrame({
  'Date': pd.date_range(start='2024-01-01',periods=5,freq='D'),
  'Volume':[1000,1100,1050,1150,1200]
})
market_volume.set_index('Date',inplace=True)
print("Stock Prices Data:")
print(stock_prices)
print("\nMarked Volume Data:")
print(market_volume)
joined_data = stock_prices.join(market_volume,how='inner')
print("\n.Joined Stock Prices and Market Volume Data:")
print(joined_data)

#concatenating
consolidated_sales = pd.concat([sales_region_1,sales_region_2],axis=0)
print("\nConsolidated Sales Data:")
print(consolidated_sales)

OUTPUT:
Employee Details:
   Employee ID     Name   Department
0          101    Alice           HR
1          102      Bob  Engineering
2          103  Charlie  Engineering
3          104    David           HR
4          105      Eva    Marketing

Employee Salaries:
   Employee ID  Salary
0          101   50000
1          102   70000
2          103   80000
3          104   55000
4          105   60000

Sales region 1:
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350

Sales region 2:
        Date Region  Sales
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  SOuth    310

Average Salary per Department:
Department
Engineering    75000.0
HR             52500.0
Marketing      60000.0
Name: Salary, dtype: float64

Merged Employee Data:
   Employee ID     Name   Department  Salary
0          101    Alice           HR   50000
1          102      Bob  Engineering   70000
2          103  Charlie  Engineering   80000
3          104    David           HR   55000
4          105      Eva
