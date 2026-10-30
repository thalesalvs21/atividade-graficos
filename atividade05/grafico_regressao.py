import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados_regressao.csv")

sns.regplot(data=df, x="renda_mensal", y="gasto_mensal", line_kws={"color": "red"})
plt.title("Renda mensal x Gasto mensal")
plt.xlabel("Renda mensal")
plt.ylabel("Gasto mensal")
plt.show()
