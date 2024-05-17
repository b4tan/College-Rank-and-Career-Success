import pandas as pd

scorecard = pd.read_csv('College_Scorecard_Data.csv')

rankings = pd.read_csv('worldUniRankings_USA-1.csv')

# Rename institution column and filter scorecard to only contain institutions in rankings
scorecard = scorecard[
  scorecard['INSTNM']
  .isin(rankings['Institution'])
  ]

# Rename column for join
rankings = rankings.rename({'Institution' : 'INSTNM'},axis=1)

combined = (
  pd.merge(scorecard, rankings, how='outer')
  .rename({'index' : 'rank'}, axis=1)     
  .set_index('rank')
  .sort_index()
)

print("Shape", combined.shape)
print(combined.head())
