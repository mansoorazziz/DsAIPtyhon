# EDA Analysis Module
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8')
sns.set_palette('husl')
# print("EDA Analysis module loaded successfully.")

# Function to load data
df = pd.read_csv('retail_sales.csv')
# print("Data loaded successfully. Here's a preview:")
# print(df.head(10))

# Data set shape and info
# print(f"Data shape: {df.shape}")
# print("Data info:")
# print(df.info())
# print('dtype of each column:')
# print(df.dtypes)

# Check for missing values
# print("Missing values in each column:")
# print(df.isnull().sum())
# print(df.info())

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
# Extract year and month from 'Date' column
# df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Quarter'] = df['Date'].dt.quarter
df['DayOfWeek'] = df['Date'].dt.day_name
df['MonthName'] = df['Date'].dt.month_name

# print("Date column converted to datetime format and new time-based features created.")

# numerical columns are properly formatted
numerical_cols = ['Sales', 'Quantity', 'Profit']
for col in numerical_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')   
# print("Numerical columns converted to numeric data types.")
# print(df.dtypes)

# date range
# print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")

# describe numrical columns
# print("Summary statistics for numerical columns:")
# print(df[numerical_cols].describe())

# catagory wise summary
# print("Summary statistics for categorical columns:")
# Category_wise_summary = df.groupby('Category').agg({'Sales': ['mean', 'sum', 'count', 'std'], 'Profit': ['mean', 'sum'], 'Quantity': ['mean', 'sum']}).round(2)
# print("Category-wise summary statistics:")
# print(Category_wise_summary)

# Region-wise summary statistics
region_summary = df.groupby('Region').agg({'Sales': ['mean', 'sum'], 'Profit': ['mean', 'sum']}).round(2)
print("Region-wise summary statistics:")
print(region_summary)