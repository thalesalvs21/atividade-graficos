import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados_frequencia.csv")

# ordena do tipo que mais aparece para o que menos aparece
ordem = df["tipo_atendimento"].value_counts().index

sns.countplot(data=df, x="tipo_atendimento", order=ordem)
plt.title("Chamados por tipo de atendimento")
plt.xlabel("Tipo de atendimento")
plt.ylabel("Quantidade")
plt.show()
