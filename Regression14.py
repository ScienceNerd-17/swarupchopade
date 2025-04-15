
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
# Create sample dataset
data = {
    "Size (sq ft)": [850, 900, 1200, 1500, 1800, 2000, 2200, 2500, 2700, 3000],
    "Price (in lakhs)": [35, 40, 50, 65, 75, 85, 95, 110, 125, 140]
}
df = pd.DataFrame(data)
print(df.head())  # Display first few rows
# Summary statistics
print(df.describe())
# Visualize the data
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Size (sq ft)"], y=df["Price (in lakhs)"])
plt.xlabel("Size (sq ft)")
plt.ylabel("Price (in lakhs)")
plt.title("House Size vs. Price")
plt.show()
# Split data into independent variable (X) and dependent variable (y)
X = df[["Size (sq ft)"]]  # Features
y = df["Price (in lakhs)"]  # Target
# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize and train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
# Predict price for a new house size
new_house_size = np.array([[700]])  # Example input
predicted_price = model.predict(new_house_size)
print("Predicted Price for 700 sq ft: "+str(predicted_price[0])+ "lakhs")
new_house_size = np.array([[3000]])  # Example input
predicted_price = model.predict(new_house_size)
# Print formatted output
print(f"Predicted Price for 3000 sq ft: {predicted_price[0]:.4f} lakhs")


