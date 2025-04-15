
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Sample DataFrame with missing values
data = {
    'Age': [100, 90, np.nan, 95],
    'Second Score': [30, 45, 56, np.nan],
    'Third Score': [np.nan, 40, 80, 98]
}
df = pd.DataFrame(data)

# 1. Handling Missing Data
print("Missing Values Before Handling:")
print(df.isnull().sum())

# Handling missing values for both numeric and categorical columns
df.fillna(df.select_dtypes(include=[np.number]).mean(), inplace=True)
print("Missing Values After Handling:")
print(df.isnull().sum())

# 2. Transforming Data
# Example transformation using apply()
df['Age_Doubled'] = df['Age'].apply(lambda x: x * 2 if pd.notnull(x) else x)
# Example transformation using map()
df['Score_Category'] = df['Second Score'].map(lambda x: 'High' if x > 40 else 'Low')

# 3. Detecting & Filtering Outliers
for col in df.select_dtypes(include=[np.number]).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
print("Outliers removed from all numeric columns.")

# 4. Vectorized String Operations
df['Score_Category'] = df['Score_Category'].str.lower()
df['Contains_High'] = df['Score_Category'].str.contains('high', na=False)
df['Category_Length'] = df['Score_Category'].str.len()

# 5. Data Visualization
plt.figure(figsize=(10, 6))
# Line Plot
plt.subplot(2, 3, 1)
plt.plot(df.index, df['Age'])
plt.title('Line Plot of Age')
# Bar Plot
plt.subplot(2, 3, 2)
plt.bar(df.index, df['Second Score'])
plt.title('Bar Plot of Second Score')
# Histogram
plt.subplot(2, 3, 3)
plt.hist(df['Third Score'].dropna(), bins=10, edgecolor='black')
plt.title('Histogram of Third Score')
# Density Plot
plt.subplot(2, 3, 4)
df['Second Score'].dropna().plot(kind='density')
plt.title('Density Plot of Second Score')
# Scatter Plot
plt.subplot(2, 3, 5)
plt.scatter(df['Age'], df['Second Score'])
plt.title('Scatter Plot: Age vs Second Score')
plt.tight_layout()
plt.show()
