import seaborn as sns
from scipy.stats import shapiro
from scipy.stats.stats import pearsonr
from scipy.stats import stats
tips = sns.load_dataset('tips')
df = tips.copy()


print(df.head())

df["total_bill"] = df["total_bill"] - df["tip"]
print(df.plot.scatter("tip","total_bill"))
print()
print()

test_istatistigi, pvalue = shapiro(df["tip"])
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

test_istatistigi, pvalue = shapiro(df["total_bill"])
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

#Correlation Coefficient
print(df["tip"].corr(df["total_bill"]))
print(df["tip"].corr(df["total_bill"], method = "spearman"))

#Correlation Significance Test

test_istatistigi, pvalue = pearsonr(df["tip"],df["total_bill"])
print('Korelasyon Katsayısı = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))


#Nonparametric Hypothesis Testing
print(stats.spearmanr(df["tip"],df["total_bill"]))
test_istatistigi, pvalue = stats.spearmanr(df["tip"],df["total_bill"])
print('Korelasyon Katsayısı = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))
test_istatistigi, pvalue = stats.kendalltau(df["tip"],df["total_bill"])
print('Korelasyon Katsayısı = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))



