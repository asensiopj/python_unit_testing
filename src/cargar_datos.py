# %%
import pandas as pd

# %%
df = pd.read_csv("googleplaystore.csv", sep=",")

# %%
def remove_nan(c, column):
    c = c.dropna(inplace=True)

remove_nan(df, "Rating")

# %%
df.reset_index(drop=True, inplace = True)

