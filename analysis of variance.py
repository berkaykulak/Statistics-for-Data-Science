import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import shapiro
import scipy.stats as stats
from scipy.stats import f_oneway
from scipy.stats import kruskal

A = pd.DataFrame([28,33,30,29,28,29,27,31,30,32,28,33,25,29,27,31,31,30,31,34,30,32,31,34,28,32,31,28,33,29])

B = pd.DataFrame([31,32,30,30,33,32,34,27,36,30,31,30,38,29,30,34,34,31,35,35,33,30,28,29,26,37,31,28,34,33])

C = pd.DataFrame([40,33,38,41,42,43,38,35,39,39,36,34,35,40,38,36,39,36,33,35,38,35,40,40,39,38,38,43,40,42])

dfs = [A, B, C]

ABC = pd.concat(dfs, axis = 1)
ABC.columns = ["GRUP_A","GRUP_B","GRUP_C"]
ABC.head()

print(shapiro(ABC["GRUP_A"]))
print(shapiro(ABC["GRUP_B"]))
print(stats.levene(ABC["GRUP_A"], ABC["GRUP_B"],ABC["GRUP_C"]))
print(f_oneway(ABC["GRUP_A"], ABC["GRUP_B"],ABC["GRUP_C"]))
print('{:.5f}'.format(f_oneway(ABC["GRUP_A"], ABC["GRUP_B"],ABC["GRUP_C"])[1]))
print(ABC.describe().T)
print(kruskal(ABC["GRUP_A"], ABC["GRUP_B"],ABC["GRUP_C"]))



