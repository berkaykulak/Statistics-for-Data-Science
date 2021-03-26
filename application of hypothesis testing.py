from scipy.stats import shapiro
import scipy.stats as stats
import numpy as np


olcumler = np.array([17, 160, 234, 149, 145, 107, 197, 75, 201, 225, 211, 119,
              157, 145, 127, 244, 163, 114, 145,  65, 112, 185, 202, 146,
              203, 224, 203, 114, 188, 156, 187, 154, 177, 95, 165, 50, 110,
              216, 138, 151, 166, 135, 155, 84, 251, 173, 131, 207, 121, 120])

print(stats.ttest_1samp(olcumler, popmean = 170))