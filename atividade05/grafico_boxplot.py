import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados_boxplot.csv")

sns.boxplot(data=df, x="departamento", y="salario")
plt.title("Salários por departamento")
plt.xlabel("Departamento")
plt.ylabel("Salário")
plt.show()
