import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Caminho corrigido para o arquivo CSV
data_path = 'BaseSayoPillow.csv'

# Carregar dados
df = pd.read_csv(data_path)

# Título
st.title('Análise dos Dados do Projeto SaYoPillow')

# Seção de gráficos
st.header('Histograma da Frequência Cardíaca')
fig, ax = plt.subplots()
sns.histplot(df['Frequência Cardíaca'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# Tabelas no final
st.header('Dados Brutos')
st.write(df)




