import matplotlib.pyplot as plt
import pandas as pd

# load data
csv_path = 'AmesHousing.csv'
df = pd.read_csv(csv_path)

# plot
plt.figure(figsize=(8,6))
plt.scatter(df['Bedroom AbvGr'], df['SalePrice'], marker='o')
plt.title("Bedroom AbvGr -> Sale Price")
plt.xlabel("bedroom")
plt.ylabel("price")
plt.show()