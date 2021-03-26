from scipy.stats import poisson

lambda_ = 0.1

rv = poisson(mu = lambda_)
print(rv.pmf(k = 0))
print(rv.pmf(k = 3))

print(rv.pmf(k = 5))

