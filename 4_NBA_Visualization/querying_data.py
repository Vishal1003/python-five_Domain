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
print(df.shape)

print(df["difference"].max())



