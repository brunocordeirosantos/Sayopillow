import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
data_path = 'BaseSayoPillow.csv'
df = pd.read_csv(data_path)

# Renomear as colunas para serem mais descritivas em português
df.columns = [
    'Faixa de Ronco', 
    'Taxa de Respiração', 
    'Temperatura Corporal', 
    'Taxa de Movimento dos Membros', 
    'Níveis de Oxigênio no Sangue', 
    'Movimento dos Olhos', 
    'Horas de Sono', 
    'Frequência Cardíaca', 
    'Nível de Estresse'
]

# Filtro de intervalo de registros
time_range = st.slider('Selecione o intervalo de registros', 0, len(df), (0, 100))

# Filtrar dados com base no intervalo de registros selecionado
filtered_df = df.iloc[time_range[0]:time_range[1]].copy()

# Histograma para Frequência Cardíaca
st.header('Distribuição da Frequência Cardíaca')
fig, ax = plt.subplots()
sns.histplot(filtered_df['Frequência Cardíaca'], bins=30, kde=True, ax=ax)
ax.set_xlabel('Frequência Cardíaca')
ax.set_ylabel('Contagem')
st.pyplot(fig)

# Gráfico de Dispersão para Correlação entre Parâmetros
st.header('Correlação entre Horas de Sono e Nível de Estresse')
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='Horas de Sono', y='Nível de Estresse', ax=ax)
st.pyplot(fig)

st.header('Correlação entre Movimento dos Olhos e Nível de Estresse')
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='Movimento dos Olhos', y='Nível de Estresse', ax=ax)
st.pyplot(fig)

# Exibir o dataframe com colunas renomeadas
st.write("Nomes das Colunas no Dataframe", df.columns)
st.write("Dados do Projeto SaYoPillow", df)


