import pandas as pd

df = pd.read_excel("demo_file.xlsx")

df.head()
df.info()

df.to_excel("my_file.xlsx", index=True)
df.to_csv("my_file.csv", index=True)