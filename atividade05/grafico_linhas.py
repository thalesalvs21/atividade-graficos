import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados_linhas.csv")
df["data"] = pd.to_datetime(df["data"])

sns.lineplot(data=df, x="data", y="vendas", hue="loja")
plt.title("Vendas por dia")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.xticks(rotation=45)
plt.show()
