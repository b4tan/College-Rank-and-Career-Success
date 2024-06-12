import pandas as pd

df = pd.read_csv('CollegeScorecardDataDictionary.csv')
df = df[['Variable Name','MERGED_2018-19 datafile']]
df.dropna(how='any')
print(df.shape) 
print(df['Variable Name'])
df = df.rename({'MERGED_2018-19 datafile':'description'}, axis=1)
print(f"Value counts\n", df['description'].value_counts())

vars = pd.read_csv('ScorecardVars.csv')

combined = pd.merge(vars,df, how='right', left_on='VARIABLE NAME', right_on='Variable Name')
print(combined.shape)

combined.to_csv('variables.csv')