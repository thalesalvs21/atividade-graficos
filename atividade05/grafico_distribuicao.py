import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados_distribuicao.csv")

sns.histplot(data=df, x="idade", bins=15)
plt.title("Distribuição da idade dos clientes")
plt.xlabel("Idade")
plt.ylabel("Quantidade")
plt.show()
