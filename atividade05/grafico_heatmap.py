import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados_heatmap.csv")

# coloca os dias da semana na ordem certa
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
tabela = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
tabela = tabela.reindex(dias)

sns.heatmap(tabela, annot=True, fmt="d", cmap="YlOrRd")
plt.title("Movimento de clientes por dia e horário")
plt.xlabel("Horário")
plt.ylabel("Dia da semana")
plt.show()
