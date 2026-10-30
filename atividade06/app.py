import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

st.sidebar.title("Informações do aluno")
st.sidebar.write("Nome: Thales Alves Gomes")
st.sidebar.write("Número da chamada: 33")
st.sidebar.write("Turma: 3E2")

st.title("Dashboard de gráficos")

# primeira linha
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Faturamento por canal")
    df = pd.read_csv("dados_pizza.csv")
    fig, ax = plt.subplots()
    ax.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%")
    st.pyplot(fig)
    st.write("O site é o canal que mais fatura, com 37,5% do total, seguido da loja física. "
             "O telefone é o canal que menos fatura.")

with col2:
    st.subheader("Movimento de clientes")
    df = pd.read_csv("dados_heatmap.csv")
    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    tabela = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
    tabela = tabela.reindex(dias)
    fig, ax = plt.subplots()
    sns.heatmap(tabela, annot=True, fmt="d", cmap="YlOrRd", ax=ax)
    ax.set_xlabel("Horário")
    ax.set_ylabel("Dia da semana")
    st.pyplot(fig)
    st.write("Sábado e domingo têm muito mais movimento que os outros dias. "
             "O maior pico é no domingo às 12h, e a quinta é o dia mais fraco.")

with col3:
    st.subheader("Vendas por dia")
    df = pd.read_csv("dados_linhas.csv")
    df["data"] = pd.to_datetime(df["data"])
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x="data", y="vendas", hue="loja", ax=ax)
    ax.tick_params(axis="x", rotation=45)
    st.pyplot(fig)
    st.write("As vendas cresceram bastante de janeiro até março, saindo de uns 100 "
             "para mais de 250 por dia. As duas lojas vendem parecido.")

# segunda linha
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Renda x Gasto")
    df = pd.read_csv("dados_regressao.csv")
    fig, ax = plt.subplots()
    sns.regplot(data=df, x="renda_mensal", y="gasto_mensal", line_kws={"color": "red"}, ax=ax)
    st.pyplot(fig)
    st.write("Quanto maior a renda, maior o gasto. Os pontos ficam bem perto da reta, "
             "então a relação entre as duas coisas é bem forte.")

with col2:
    st.subheader("Vendas por categoria e região")
    df = pd.read_csv("dados_barras.csv")
    fig, ax = plt.subplots()
    sns.barplot(data=df, x="categoria", y="vendas_medias", hue="regiao", ax=ax)
    st.pyplot(fig)
    st.write("A região Oeste é a que mais vende na maioria das categorias e a Norte é a que menos vende. "
             "Eletrônicos é diferente, vende mais no Leste.")

with col3:
    st.subheader("Salários por departamento")
    df = pd.read_csv("dados_boxplot.csv")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="departamento", y="salario", ax=ax)
    st.pyplot(fig)
    st.write("TI e Vendas pagam mais que Marketing e RH. Todos os departamentos têm "
             "alguns salários muito acima dos outros, que aparecem como bolinhas.")

# terceira linha
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Altura x Peso")
    df = pd.read_csv("dados_dispersao.csv")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="altura_cm", y="peso_kg", hue="sexo", ax=ax)
    st.pyplot(fig)
    st.write("Quem é mais alto costuma pesar mais. Os pontos de homens e mulheres "
             "estão misturados, sem muita diferença entre os dois.")

with col2:
    st.subheader("Idade dos clientes")
    df = pd.read_csv("dados_distribuicao.csv")
    fig, ax = plt.subplots()
    sns.histplot(data=df, x="idade", bins=15, ax=ax)
    st.pyplot(fig)
    st.write("A maioria dos clientes tem entre 20 e 30 anos, mas também tem "
             "um grupo grande entre 40 e 55 anos.")

with col3:
    st.subheader("Chamados por tipo")
    df = pd.read_csv("dados_frequencia.csv")
    ordem = df["tipo_atendimento"].value_counts().index
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="tipo_atendimento", order=ordem, ax=ax)
    st.pyplot(fig)
    st.write("Dúvida é o tipo de chamado mais comum, depois vem reclamação. "
             "Elogio é o que menos aparece.")
