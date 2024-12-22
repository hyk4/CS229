import matplotlib.pyplot as plt
import pandas as pd

# load data
file_name = 'HousePrices.csv'
df = pd.read_csv(file_name)

# select necessary columns
df = df[['GrLivArea', 'LotArea', 'Dwell_Type']]
df = df[df['LotArea'] <= 20000]

# map type 20 and 160 to circle and triangle markers
markers = { 20: 'o', 160: '^' }

# set colors for each type
colors = { 20: 'blue', 160: 'orange' }

# plot
plt.figure(figsize=(8, 6))
for house_type in df['Dwell_Type'].unique():
    if house_type not in markers:
        continue
    subset = df[df['Dwell_Type'] == house_type]
    plt.scatter(
        subset['GrLivArea'],
        subset['LotArea'],
        label=house_type,
        marker=markers[house_type],
        color=colors.get(house_type, 'gray'),
        s=100)
plt.xlabel('area(ft²)', fontsize=12)
plt.ylabel('lot size', fontsize=12)
plt.title('House Type Classification', fontsize=14)
plt.legend(title='Dwell_Type')
plt.grid(True)
plt.show()