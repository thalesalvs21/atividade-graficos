import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_pizza.csv")

plt.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%")
plt.title("Faturamento por canal de venda")
plt.show()
