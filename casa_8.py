# https://www.youtube.com/watch?v=mT-2AxZLtvw&t=7s

import pandas as pd
df = pd.read_csv("big-mac-full-index.csv")
# print(df.head())

# using iterrows()
for i,r in df.iterrows():
    print(r[r"date"],
          r["iso_a3"])
# r is the row

# using apply()
print(df.apply(lambda row: row ["iso_a3"], axis = 1))
# axis = y-axis