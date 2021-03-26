from scipy.stats import norm


print(1-norm.cdf(90, 80, 5))
print(1-norm.cdf(70, 80, 5))
print(norm.cdf(73, 80, 5))
print(norm.cdf(90, 80, 5) - norm.cdf(85, 80, 5))



