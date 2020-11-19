# %%
import os
import pytest
import numpy as np
import pandas as pd

# %%
df = pd.read_csv("../../src/data/googleplaystore.csv", sep=",") # we go up 2 levels because it takes the real current level
        

# %%
print(df)