import numpy as np
fiyatlar = np.random.randint(10,110, 1000)
import statsmodels.stats.api as sms

print(fiyatlar.mean())

print(sms.DescrStatsW(fiyatlar).tconfint_mean())
def yazdir(metin):
    print(metin, "program öğrenilecek")

yazdir("O")
print("metin", "program öğrenilecek")
