import matplotlib.pyplot as plt
import pandas as pd

sample = [{"id": 1, "month": 3, "day": 4, "kcal": 166, "step": 42},
        {"id": 7777, "month": 5, "day": 7, "kcal": 126, "step": 422},
        {"id": 771, "month": 9, "day": 3, "kcal": 1260, "step": 4},
        {"id": 3, "month": 5, "day": 2, "kcal": 1663, "step": 424}]

#月指定->

df = pd.DataFrame(sample)
df['date'] = df['month'].astype(str).str.cat(df['day'].astype(str), sep='/')
df_s = df.sort_values(['day', 'month'], ascending=[False, False])
print(df_s)
df_s.plot.bar('day', 'kcal')
plt.savefig("test.png")
