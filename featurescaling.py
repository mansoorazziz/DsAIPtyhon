
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv('telecom_customer_churn_feature_engineering.csv')
# print(df[['monthly_income', 'monthly_bill']].head())
# print(df[['monthly_income', 'monthly_bill']].describe())
# Standardization
# imcomeMean = df['monthly_income'].mean()
# incomeStd = df['monthly_income'].std()
# # print('Mean:', imcomeMean)
# print('Standard Deviation:', incomeStd)

# df['monthly_income_zscore'] = (df['monthly_income'] - imcomeMean) / incomeStd
# print(df[['monthly_income', 'monthly_income_zscore']].head())
# print(df['monthly_income_zscore'].mean(), df['monthly_income_zscore'].std())

# minMaxScaler = MinMaxScaler()
# bill_min = df['monthly_bill'].min()
# bill_max = df['monthly_bill'].max()
# # print('Min:', bill_min)
# # print('Max:', bill_max)

# # min Max Formula
# df['monthly_bill_minmax'] = (df['monthly_bill'] - bill_min) / (bill_max - bill_min)
# # print(df[['monthly_bill', 'monthly_bill_minmax']].head())
# monthly_bill_minmax_mean = df['monthly_bill_minmax'].min()
# monthly_bill_minmax_std = df['monthly_bill_minmax'].max()  
# print('Mean:', monthly_bill_minmax_mean)
# print('Standard Deviation:', monthly_bill_minmax_std)

# taking log of monthly income to reduce skewness
df['monthly_income_log'] = np.log(df['monthly_income'])
print(df[['monthly_income', 'monthly_income_log']].head())