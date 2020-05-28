import pandas as pd
import numpy as np

nba = pd.read_csv('nbaallelo.csv')

# This will give all the datas (no ...)
pd.set_option("display.max.column", None)
pd.set_option("display.precision", 2)

# Games played after 2010
# new_games = nba[nba["year_id"] > 2010]
# print(new_games)

# Not a null 
# games_no_null = nba[nba["notes"].notnull()]
# print(games_no_null.shape)


# Multiple Queries :
# print(nba[
#     (nba["team_id"] == "BLB") & 
#     (nba["pts"] > 100) &
#     (nba["opp_pts"] > 100) &
#     (nba["_iscopy"] == 0)
# ])

# ================================ Manipulating DATA ===================================

df = nba.copy()

# Adding new col
df["difference"] = df.pts - df.opp_pts 
# print(df.shape)
# print(df["difference"].max())

# rename_data = df.rename(columns = {"game_result" : "result", "game_location" : "location"})
# print(rename_data.info())



# delete some columns
elo_columns = ["elo_i", "elo_n", "opp_elo_i", "opp_elo_n"]
df.drop(elo_columns, inplace= True, axis = 1)


# print(df["game_location"].nunique())
# print(df["game_location"].value_counts())


# ===================== Important ==============================

# Converting the data in categorical data
## Converting game location from object to categorical

df["game_location"] = pd.Categorical(df["game_location"])
# print(df["game_location"].dtype)

# Cleaning data
"""
Naive Approach  
rows_with_noNull = nba.dropna()
print(rows_with_noNull)
"""

data_with_dfVal = nba.copy()
data_with_dfVal["notes"].fillna(
    value = "NaN",
    inplace = True
)

print(data_with_dfVal["notes"].describe())
