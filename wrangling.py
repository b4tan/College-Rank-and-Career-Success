import pandas as pd
import numpy as np

scorecard = pd.read_csv('College_Scorecard_Data.csv')
scorecard.head()
print(scorecard.shape)

rankings = pd.read_csv('worldUniRankings_USA-1.csv')

print("Rankings shape", rankings.shape)

scorecard = scorecard[scorecard['INSTNM'].isin(rankings['Institution'])].reset_index()
scorecard = scorecard.dropna(axis=1, how='any')
print("Scorecard shape:", scorecard.shape)

rankings = rankings.rename({'Institution' : 'INSTNM'},axis=1)
print(rankings.columns)

data = pd.merge(scorecard, rankings, how='outer')

data = data.set_index('INSTNM')
data = data.rename({'index' : 'rank'}, axis=1)
print(data)
