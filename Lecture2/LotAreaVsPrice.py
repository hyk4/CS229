import pandas as pd
import matplotlib.pyplot as plt

# load data
csv_path = 'AmesHousing.csv'
df = pd.read_csv(csv_path)

# plot
plt.figure(figsize=(8,6))
plt.scatter(df['Lot Area'], df['SalePrice'], marker='o')
plt.title("Lot Area -> Sale Price")
plt.xlabel("area(ft²)")
plt.ylabel("price")
plt.show()