import pandas as pd
import numpy as np

# NBA Data visualization
nba = pd.read_csv('nbaallelo.csv')

# print(len(nba))
# print(nba.shape)

# print(nba.head(2))  # Displaying 2 datas from the top

# ================ Visualization Start ==================
 # data types of all the data
# print(nba.info()) 

"""
OUTPUT :
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 126314 entries, 0 to 126313
Data columns (total 23 columns):
 #   Column         Non-Null Count   Dtype
---  ------         --------------   -----
 0   gameorder      126314 non-null  int64
 1   game_id        126314 non-null  object
 2   lg_id          126314 non-null  object
 3   _iscopy        126314 non-null  int64
 4   year_id        126314 non-null  int64
 5   date_game      126314 non-null  object
 6   seasongame     126314 non-null  int64
 7   is_playoffs    126314 non-null  int64
 8   team_id        126314 non-null  object
 9   fran_id        126314 non-null  object
 10  pts            126314 non-null  int64
 11  elo_i          126314 non-null  float64
 12  elo_n          126314 non-null  float64
 13  win_equiv      126314 non-null  float64
 14  opp_id         126314 non-null  object
 15  opp_fran       126314 non-null  object
 16  opp_pts        126314 non-null  int64
 17  opp_elo_i      126314 non-null  float64
 18  opp_elo_n      126314 non-null  float64
 19  game_location  126314 non-null  object
 20  game_result    126314 non-null  object
 21  forecast       126314 non-null  float64
 22  notes          5424 non-null    object
dtypes: float64(6), int64(7), object(10)
memory usage: 22.2+ MB
None

"""

# Statistics of the data
# print(nba.describe()) 
"""
OUTPUT :
  gameorder        _iscopy        year_id     seasongame  ...        opp_pts      opp_elo_i      opp_elo_n       forecast
count  126314.000000  126314.000000  126314.000000  126314.000000  ...  126314.000000  126314.000000  126314.000000  126314.000000
mean    31579.000000       0.500000    1988.200374      43.533733  ...     102.729982    1495.236055    1495.236055       0.500000
std     18231.927643       0.500002      17.582309      25.375178  ...      14.814845     112.139945     112.461687       0.215252
min         1.000000       0.000000    1947.000000       1.000000  ...       0.000000    1091.644500    1085.774400       0.020447
25%     15790.000000       0.000000    1975.000000      22.000000  ...      93.000000    1417.237975    1416.994900       0.327989
50%     31579.000000       0.500000    1990.000000      43.000000  ...     103.000000    1500.945550    1500.954400       0.500000
75%     47368.000000       1.000000    2003.000000      65.000000  ...     112.000000    1576.060000    1576.291625       0.672011
max     63157.000000       1.000000    2015.000000     108.000000  ...     186.000000    1853.104500    1853.104500       0.979553

"""

# This will give all the datas (no ...)
pd.set_option("display.max.column", None)
pd.set_option("display.precision", 2)


print(nba.describe(include = np.object))
# print("====================================")

# print(nba['team_id'].value_counts())
# print("====================================")

# print(nba['fran_id'].value_counts())
# print("====================================")



# Getting all the teams of one kind (eg: Lakers)
print(nba.loc[nba['fran_id'] == "Lakers", "team_id"].value_counts())

"""
LAL    5078
MNL     946
Name: team_id, dtype: int64

===>> From above data one can assume or guess that MNL have stopped playing since their game is very less.
 So now we will be checking the time.
"""

print("===========================")

# print(nba.loc[nba['team_id'] == "MNL", "date_game"].min())  # first date
# print(nba.loc[nba['team_id'] == "MNL", "date_game"].max())  # last date

"""
From above we get the MNL played only for 10 yrs.
"""

# Total points of BOS
print(nba.loc[nba['team_id'] == 'BOS','pts'].sum())





