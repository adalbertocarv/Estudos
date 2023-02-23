import pandas as pd


# Lê os arquivos CSV
df1 = pd.read_csv('zbx_devices_edit2.csv')
df2 = pd.read_csv('zbx_virtual_devices.csv')



# Definindo as funções

def check_empty_rows(df):
    empty_rows = df.isnull().all(axis=1)
    if empty_rows.any():
        print(f"Linhas vazias encontradas na planilha:")
        print(df[empty_rows])

def check_empty_cells(df):
    empty_cells = df.isnull().sum().sum()
    if empty_cells > 0:
        print(f'Existem {empty_cells} células vazias na tabela.')
        empty_cells_per_column = df.isnull().sum()
        print('Células vazias por coluna:')
        print(empty_cells_per_column)


def check_trailing_spaces(df):
    trailing_spaces_per_column = df.apply(lambda x: x.astype(str).str.endswith(' ').sum())
    if trailing_spaces_per_column.any():
        print(f"Valores com espaços vazios encontrados nas colunas:")
        print(trailing_spaces_per_column)

# Verifica se há linhas vazias na tabela 1
check_empty_rows(df1)

# Verifica se há linhas vazias na tabela 2
check_empty_rows(df2)

# Verifica se há células vazias na tabela 1
check_empty_cells(df1)

# Verifica se há células vazias na tabela 2
check_empty_cells(df2)

# Verifica se há espaços vazios no final das strings em cada coluna da tabela 1
print("Tabela 1:")
check_trailing_spaces(df1)

# Verifica se há espaços vazios no final das strings em cada coluna da tabela 2
print("\nTabela 2:")
check_trailing_spaces(df2)

# Definir a coluna a ser comparada
coluna_comparacao = 'mac'

# Encontrar os valores que se repetem nas duas tabelas
valores_repetidos = pd.Series(list(set(df1[coluna_comparacao]) & set(df2[coluna_comparacao])))

# Verificar se há linhas com o mesmo valor na coluna de interesse
macs_repetidos = df1[df1[coluna_comparacao].isin(valores_repetidos)]

# Imprimir as linhas repetidas
print(f"Macs repetidos:")
print(macs_repetidos)