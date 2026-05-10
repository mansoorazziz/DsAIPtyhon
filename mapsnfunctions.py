
import pandas as pd

sales_data = pd.read_csv("sales.csv", parse_dates=['order_date'] )
sales_data = sales_data.set_index('order_date')
monthly_revenue = sales_data['revenue'].resample('ME').sum()
# print(monthly_revenue.pct_change())
print(monthly_revenue.index.is_monotonic_increasing)
# print(sales_data.index)
# print(monthly_revenue)

# print(sales_data.info())

# def add_net_revenue(data):
#     data['net_revenue'] = data['revenue'] - data['profit']
#     return data

# def add_profit(data):
#     data['profit'] = data['revenue'] * 0.2
#     return data

# sales_data = sales_data.pipe(add_profit).pipe(add_net_revenue)
# print(sales_data[['revenue','net_revenue', 'profit']].head())


# sales_data['payment_type'] = sales_data['payment_method'].map({'Card':'Digital', 'COD':'Cash', 'Wallet':'Digital'})
# sales_data['payment_type'].unique()


# print(sales_data[['payment_method', 'payment_type']].head())
# print(sales_data.groupby('payment_type').size())

# def revenue_category(row):
#     if row['revenue'] > 500:
#         return 'High'
#     elif row['revenue'] >= 200:
#         return 'Medium'
#     else:
#         return 'Low'
    
# sales_data['revenue_category'] = sales_data.apply(revenue_category, axis=1)
# print(sales_data[['revenue', 'revenue_category']].head())
# print(sales_data['revenue_category'].value_counts())