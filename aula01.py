import pandas as pd;

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
print("--------------------------------")
print(df["senioridade"].value_counts())
print("--------------------------------")
print(df["contrato"].value_counts())
print("--------------------------------")
print(df["remoto"].value_counts())
print("--------------------------------")
print(df["tamanho_empresa"].value_counts())
print("--------------------------------")

senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)
print(df['senioridade'].value_counts())
print("--------------------------------")

contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}
df['contrato'] = df['contrato'].replace(contrato)
print(df['contrato'].value_counts())
print("--------------------------------")

tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'

}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
print(df['tamanho_empresa'].value_counts())
print("--------------------------------")

mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}

df['remoto'] = df['remoto'].replace(mapa_trabalho)
print(df['remoto'].value_counts())
print("--------------------------------")

print(df.head())

print("--------------------------------")

print(df.describe(include='object'))
