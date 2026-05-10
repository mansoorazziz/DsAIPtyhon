import pandas as pd
df = pd.read_csv('HousePricePrediction.csv')

# Handle missing values Appropriately (e.g., for numerical columns, use mean; for categorical columns, use mode)
for column in df.columns:
    if df[column].isnull().sum() > 0:
        if df[column].dtype == 'object':
            df[column] = df[column].fillna(df[column].mode()[0])
        else:
            df[column] = df[column].fillna(df[column].mean())

# Question #5 : Data Preprocessing
# 1. Convert categorical variables into numerical form (encoding)
categorical_columns = df.select_dtypes(include=['object']).columns
for column in categorical_columns:
    df[column] = df[column].astype('category').cat.codes
# 2.Preparing the dataset for machine learning and display it’s preview in the output
print(df.head(10))




# # Question #4. Feature Selection
# # 1. Identify relevant features for analysis
# relevant_features = ['LotArea', 'OverallCond', 'BldgType', 'TotalBsmtSF', 'YearBuilt']
# # 2. Remove unnecessary columns such as identifiers (e.g., Id)
# df = df[relevant_features]
# # 3. Create a new feature called "Age" by calculating the difference between the current year and the "YearBuilt" column
# current_year = pd.Timestamp.now().year 
# df['Age'] = current_year - df['YearBuilt']
# # 4. Display the first few rows of the updated DataFrame to verify the changes 
# print(df.head(10))


# Question #3 : Data Cleaning
# 1. Check for missing values in the dataset
# print("Missing values in each column:")
# print(df.isnull().sum())
# # 2. Handle missing values Appropriately (e.g., for numerical columns, use mean; for categorical columns, use mode)
# for column in df.columns:
#     if df[column].isnull().sum() > 0:
#         if df[column].dtype == 'object':
#             df[column] = df[column].fillna(df[column].mode()[0])
#         else:
#             df[column] = df[column].fillna(df[column].mean())
# print("Missing values after handling:")
# print(df.isnull().sum())
# 3. Check and remove duplicate records if any
# print("Number of duplicate records:", df.duplicated().sum())
# df = df.drop_duplicates()

# # Question #2 : Data Exploration
# #  1. Display the shape of the dataset
# print("Shape of the dataset:", df.shape)
# # 2. Check data types of all columns
# print("Data types of all columns:")
# print(df.dtypes)
# # 3. Generate summary statistics of numerical features
# print("Summary statistics of numerical features:")
# print(df.describe())


# Question # 1: Display the first few rows of the DataFrame to understand its structure and contents.
# Display the first few rows of the DataFrame
# print(df.head(10))