import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados_barras.csv")

sns.barplot(data=df, x="categoria", y="vendas_medias", hue="regiao")
plt.title("Vendas médias por categoria e região")
plt.xlabel("Categoria")
plt.ylabel("Vendas médias")
plt.show()
