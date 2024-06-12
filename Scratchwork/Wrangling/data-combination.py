# Filter the DataFrame to include only rows where the country is "USA"
rankings = rankings[rankings['Location'] == 'USA'].reset_index()

# Rename institution column and filter scorecard to only contain institutions in rankings
scorecard = scorecard[
  scorecard['INSTNM']
  .isin(rankings['Institution'])
  ]

# Rename column for join
rankings = rankings.rename({'Institution' : 'INSTNM'},axis=1)

combined = (
  pd.merge(scorecard, rankings, how='outer')
  .rename({'index' : 'RANK'}, axis=1)     
  .set_index('RANK')
  .sort_index()
)

# Generating list of columns of interest
cols_of_interest = """RANK
INSTNM
NPT41_PUB
NPT42_PUB
NPT43_PUB
NPT44_PUB
NPT45_PUB
NPT41_PRIV
NPT42_PRIV
NPT43_PRIV
NPT44_PRIV
NPT45_PRIV
NPT41_PROG
NPT42_PROG
NPT43_PROG
NPT44_PROG
NPT45_PROG
NPT41_OTHER
NPT42_OTHER
NPT43_OTHER
NPT44_OTHER
NPT45_OTHER
NPT4_048_PUB
NPT4_048_PRIV
NPT4_048_PROG
NPT4_048_OTHER
NPT4_3075_PUB
NPT4_3075_PRIV
NPT4_75UP_PUB
NPT4_75UP_PRIV
NPT4_3075_PROG
NPT4_3075_OTHER
NPT4_75UP_PROG
NPT4_75UP_OTHER
COSTT4_A
COSTT4_P
TUITIONFEE_IN
TUITIONFEE_OUT
TUITIONFEE_PROG
GRAD_DEBT_MDN
LO_INC_DEBT_MDN
MD_INC_DEBT_MDN
HI_INC_DEBT_MDN
COUNT_NWNE_3YR
COUNT_WNE_3YR
CNTOVER150_3YR
DBRR4_FED_UG_DEN
DBRR4_FED_UG_RT
DBRR5_FED_UG_NUM
DBRR5_FED_UG_DEN
DBRR10_FED_UG_NUM
DBRR10_FED_UG_DEN
DBRR20_FED_UG_NUM
DBRR20_FED_UG_DEN
DBRR1_FED_UGCOMP_NUM
DBRR1_FED_UGCOMP_DEN
BBRR1_FED_UGCOMP_MAKEPROG
BBRR1_FED_UGCOMP_PAIDINFULL
BBRR2_FED_UGCOMP_MAKEPROG
BBRR2_FED_UGCOMP_PAIDINFULL
MDCOST_ALL
MDEARN_PD
MD_EARN_WNE_1YR
MD_EARN_WNE_4YR
MDEARN_PD
MD_EARN_WNE_1YR
MD_EARN_WNE_4YR
""".split(sep='\n')

# Determine which of our interested columns are in the combined data
selected_cols = [col for col in cols_of_interest if col in combined.columns.to_list()]

# Keep only columns of interest and remove any variables that are all null
combined = combined[selected_cols].dropna(how='all', axis=0).dropna(how='all', axis=1)
print("Combined dataset shape:", combined.shape)
combined.head()