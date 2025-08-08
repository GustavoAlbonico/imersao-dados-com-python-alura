import pandas as pd;


# AULA01
print("AULA01 \n")
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
print(df.head(5))
print(df.info())
print(df.describe())
print(df.shape)

linhas, colunas = df.shape
print("linhas:", linhas)
print("colunas:", colunas)

print(df.columns)

# Dicionário de renomeação
novos_nomes = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

df.rename(columns=novos_nomes, inplace=True)
print(df.head())
print("\n")
print(df["senioridade"].value_counts())
print("\n")
print(df["contrato"].value_counts())
print("\n")
print(df["remoto"].value_counts())
print("\n")
print(df["tamanho_empresa"].value_counts())
print("\n")

senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)
print(df['senioridade'].value_counts())
print("\n")

contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}
df['contrato'] = df['contrato'].replace(contrato)
print(df['contrato'].value_counts())
print("\n")

tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'

}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
print(df['tamanho_empresa'].value_counts())
print("\n")

mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}

df['remoto'] = df['remoto'].replace(mapa_trabalho)
print(df['remoto'].value_counts())
print("\n")

print(df.head())

print("\n")

print(df.describe(include='object'))

# AULA02
print("\n AULA02 \n")

print(df.isnull().sum())
print("\n")
print(df['ano'].unique())
print("\n")
print(df[df.isnull().any(axis=1)])

import numpy as np

df_salarios = pd.DataFrame({
    'nome':["Ana","Carlos","Roberto","Lucas","Val"],
    'salario':[4000, np.nan ,5000,np.nan,100000],
})

df_salarios['salarios_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
df_salarios['salarios_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

print("\n")
print(df_salarios)

df_temperatura = pd.DataFrame({
    'dia':['Segunda','Terça','Quarta','Quinta','Sexta'],
    'temperatura':[30,np.nan, np.nan, 28, 27]
})

#foward fill completa com o valor anterior a null os campos que possuem null
df_temperatura['preenchido_ffill'] = df_temperatura['temperatura'].ffill()
#foward fill completa com o valor posterior a null os campos que possuem null
df_temperatura['preenchido_bfill'] = df_temperatura['temperatura'].bfill()
print("\n")
print(df_temperatura)
print("\n")

df_cidades = pd.DataFrame({
    'nome':["Ana","Carlos","Roberto","Lucas","Val"],
    'cidade':["São Paulo", np.nan, "Curitiba", np.nan, "Belém"]
})

''' Substuindo campos nulos por mensagem '''
df_cidades['cidade_preenchida'] = df_cidades["cidade"].fillna("Não informado")
print(df_cidades)
print("\n")

df_limpo = df.dropna() #remove dados null
print(df_limpo.isnull().sum())
print("\n")

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
print(df_limpo.info())
print("\n")

# AULA03
import seaborn as sns
import matplotlib.pyplot as plt
# df_limpo['senioridade'].value_counts().plot(kind='bar', title="Distribuição de senioridade")

'''Exemplo de gráfico 1'''
# ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index
# plt.figure(figsize=(8,5))
# sns.barplot(data= df_limpo, x='senioridade', y ='usd', order=ordem)
# plt.title('Salário médio por senioridade')
# plt.xlabel("Senioridade")
# plt.xlabel("Salário Médio Anual (USD)")
# plt.show()

'''Exemplo de gráfico 2'''
# plt.figure(figsize=(10,4))
# sns.histplot(df_limpo['usd'], bins = 50, kde=True)
# plt.title('Distruibuição dos salários anuais')
# plt.xlabel("Salário")
# plt.ylabel("Frequência")
# plt.show()

'''Exemplo de gráfico 3'''
# plt.figure(figsize=(8,5))
# sns.boxplot(x=df_limpo['usd'])
# plt.title("Boxplot Salário")
# plt.xlabel("Salário em USD")
# plt.show()

'''Exemplo de gráfico 4'''
# ordem_senioridade = ['junior', 'pleno','senior','executivo']
# plt.figure(figsize=(8,5))
# sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade)
# plt.title("Boxplot da distruibuição por senioridade")
# plt.xlabel("Salário em USD")
# plt.show()

'''Exemplo de gráfico 5 colorido'''
# ordem_senioridade = ['junior', 'pleno','senior','executivo']
# plt.figure(figsize=(8,5))
# sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
# plt.title("Boxplot da distruibuição por senioridade")
# plt.xlabel("Salário em USD")
# plt.show()

import plotly.express as px

'''Exemplo de gráfico iterativo 1'''
# senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

# fig = px.bar(senioridade_media_salario,
#              x='senioridade',
#              y='usd',
#              title='Média Salarial por Senioridade',
#              labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})
# fig.show()

'''Exemplo de gráfico iterativo 2'''
# remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
# remoto_contagem.columns = ['tipo_trabalho','quantidade']

# fig = px.pie(remoto_contagem,
#              names='tipo_trabalho',
#              values='quantidade',
#              title='Proporção dos tipos de trabalho')
# fig.show()

'''Exemplo de gráfico iterativo 3'''
# remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
# remoto_contagem.columns = ['tipo_trabalho','quantidade']

# fig = px.pie(remoto_contagem,
#              names='tipo_trabalho',
#              values='quantidade',
#              title='Proporção dos tipos de trabalho',
#              hole= 0.5)
# fig.update_traces(textinfo='percent+label')
# fig.show()
