import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# 1. Load your cleaned data from the new data/ folder
df = pd.read_excel('../data/Cleaned_Superstore.xlsx')

# 2. AI Anomaly Detection: Spotting the 'weird' transactions
iso_forest = IsolationForest(contamination=0.05, random_state=42)
df['is_anomaly'] = iso_forest.fit_predict(df[['Sales', 'Profit', 'Discount']])

# Filter to see transactions the AI thinks are outliers
anomalies = df[df['is_anomaly'] == -1]
print(f"Identified {len(anomalies)} anomalous transactions for review.")

# 3. Category Efficiency Score
df['Efficiency'] = df['Profit'] / df['Quantity']
efficiency_rank = df.groupby('Category')['Efficiency'].mean().sort_values(ascending=False)

print("\nCategory Efficiency (Profit per Unit):")
print(efficiency_rank)

# 4. Quick Visualization
plt.figure(figsize=(10, 6))
plt.scatter(df['Sales'], df['Profit'], c=df['is_anomaly'], cmap='coolwarm', alpha=0.5)
plt.title('Sales vs Profit: AI-Detected Outliers (Red)')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()
