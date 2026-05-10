
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('healthcare_patient_analytics_seaborn.csv')
numeric_df = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()
# print(correlation_matrix)

# for heatmap

# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', mask=mask)
plt.title('Correlation Heatmap')
plt.show()

# samplefor show
# sample_df = numeric_df.sample(n=100, random_state=42)
# print(sample_df.head())