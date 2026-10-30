import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados_dispersao.csv")

sns.scatterplot(data=df, x="altura_cm", y="peso_kg", hue="sexo")
plt.title("Altura x Peso")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.show()
