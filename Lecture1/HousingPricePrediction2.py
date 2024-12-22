import pandas as pd
import matplotlib.pyplot as plt

# load data
file_name = 'HousePrices.csv'
df = pd.read_csv(file_name)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['GrLivArea'], df['LotArea'], df['Property_Sale_Price'], marker='x')
ax.set_title("Housing Price Prediction")
ax.set_xlabel("area(ft²)")
ax.set_ylabel("lot size")
ax.set_zlabel("price")
plt.show()