from scipy.stats import bernoulli

p = 0.6
rv = bernoulli(p)

print(rv.pmf(k = 0))
