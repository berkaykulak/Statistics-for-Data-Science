import seaborn as sns
import researchpy as rp
tips = sns.load_dataset("tips")
df = tips.copy()

print(df.head())
print(df.describe().T)
print(rp.summary_cont(df[["total_bill","tip","size"]]))
print(rp.summary_cat(df[["sex","smoker","day"]]))
print(df[["tip","total_bill"]].cov())
print(df[["tip","total_bill"]].corr())