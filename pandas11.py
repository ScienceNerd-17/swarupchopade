
import pandas as pd
df = pd.read_csv("data.csv")
print("First 10 Records:")
print(df.head(10))
print("\nLast 10 Records:")
print(df.tail(10))

import pandas as pd
df = pd.read_csv('data.csv')
print(df.shape)
print(df.index)
print(df.columns)

import pandas as pd
df = pd.read_csv('data.csv')
df = df.drop(columns=['Pulse'])
print(df)


import pandas as pd
df = pd.read_csv('data.csv')
df_ranked = df.rank(ascending=False)
print(df_ranked)
df = df.sort_values(by='Pulse', ascending=True)
print(df)

# mean
import pandas as pd
df = pd.read_csv('data.csv')
print(df["Pulse"].mean())
#meadian
import pandas as pd
df = pd.read_csv('data.csv')
print(df["Pulse"].median())
# mode
import pandas as pd
df = pd.read_csv('data.csv')
print(df["Pulse"].mode()[0] )


import pandas as pd
df = pd.read_csv('data.csv')
print(df["Calories"].unique())
print(len(df["Calories"].unique()))

# single
import pandas as pd
df = pd.read_csv('data.csv')
print(df.columns)
df = df.rename(columns={df.columns[1]: 'Years'})
print(df)

# multiple
import pandas as pd
df = pd.read_csv('data.csv')
df=df.rename(columns={df.columns[0]: 'Student', df.columns[2]: 'Hello'})
print(df)
