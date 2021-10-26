import pandas as pd


coaches_df = pd.read_excel("Coaches.xlsx")
df1 = coaches_df.fillna(0)
print(coaches_df)