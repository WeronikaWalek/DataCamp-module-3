import pandas as pd
homelessness = pd.read_csv('homelessness.csv')
print(homelessness)
homelessness.head()
print(homelessness.head())
homelessness.info()
print(homelessness.info())
print(homelessness.shape)
print(homelessness.describe())
print(homelessness.values)
print(homelessness.columns)
print(homelessness.index)
homelessness_ind=homelessness.sort_values("individuals")
print(homelessness_ind.head())
homelessness_fam=homelessness.sort_values("family_members", ascending=False)
print(homelessness_fam.head())
homelessness_reg_fam=homelessness.sort_values(["region", "family_members"], ascending=[True, False])
print(homelessness_reg_fam.head())
individuals=homelessness["individuals"]
print(individuals.head())
state_fam=homelessness[["state", "family_members"]]
print(state_fam.head())
ind_state=homelessness[["individuals", "state"]]
print(ind_state.head())
ind_gt_10k=homelessness[homelessness["individuals"] > 10000]
print(ind_gt_10k)
mountain_reg=homelessness[homelessness["region"]== "Mountains"]
print(mountain_reg)
