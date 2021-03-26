from statsmodels.stats.proportion import proportions_ztest

count = 40
nobs = 500
value = 0.125

print(proportions_ztest(count, nobs, value))











