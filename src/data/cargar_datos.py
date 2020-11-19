# %%
import pandas as pd

# %%
def remove_nan(c, column):
    c = c.dropna(inplace=True)
""" df = pd.read_csv("googleplaystore.csv", sep=",")
remove_nan(df, "Rating")

# %%
df.reset_index(drop=True, inplace = True) """

