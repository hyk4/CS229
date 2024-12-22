import pandas as pd
import matplotlib.pyplot as plt

# load data
file_name = 'HousePrices.csv'
df = pd.read_csv(file_name)

# plot
plt.figure(figsize=(8,6))
plt.scatter(df['GrLivArea'], df['Property_Sale_Price'], marker='x')
plt.title("Housing Price Prediction")
plt.xlabel("area(ft²)")
plt.ylabel("price")
plt.show()