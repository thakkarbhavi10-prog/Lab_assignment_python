# Lab Assignment – 2 (States Data)

import pandas as pd


# Create DataFrame
data = {
    'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'UP', 'MP'],
    'Area': [307713, 196244, 342239, 243286, 308252],
    'Population': [112374333, 60439692, 68548437, 199812341, 72626809]
}

df = pd.DataFrame(data)

# a) Complete info
print("\nState Data:\n", df)

# b) Largest Area
print("\nState with Largest Area:")
print(df.loc[df['Area'].idxmax()])

# c) Largest Population
print("\nState with Largest Population:")
print(df.loc[df['Population'].idxmax()])

# d) Population Density
df['Density'] = df['Population'] / df['Area']
print("\nWith Density:\n", df)

# e) Highest Density State
print("\nState with Highest Density:")
print(df.loc[df['Density'].idxmax()])