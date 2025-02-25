import pandas as pd

# Função para leitura dos arquivos CSV
def read_csv_files():
    relevancia = pd.read_csv("entradas/Relevancia.csv")  # Arquivo de relevância com os pesos
    ee_data = pd.read_csv("entradas/EE.csv")            # Dados de EE
    sb_data = pd.read_csv("entradas/SB.csv")            # Dados de SB
    so_data = pd.read_csv("entradas/SO.csv")            # Dados de SO
    alunos_data = pd.read_csv("entradas/Alunos.csv")    # Dados dos alunos (ID e Nome)
    riscos_data = pd.read_csv("entradas/Riscos.csv")    # Dados da tabela de riscos
    return relevancia, ee_data, sb_data, so_data, alunos_data, riscos_data

# Cálculo do SMI (Índice de Monitoramento de Segurança)
def calculate_smi(df, relevancia):
    delta1, delta2, delta3 = relevancia.iloc[0, 0], relevancia.iloc[0, 1], relevancia.iloc[0, 2]
    beta = delta1 + delta2 + delta3
    df['δ1'], df['δ2'], df['δ3'] = delta1, delta2, delta3  # Adiciona os valores de delta com novos nomes de colunas
    df['SMI'] = ((delta1 * (df['EE'] * df['P1'])) + (delta2 * (df['SB'] * df['P2'])) + (delta3 * (df['SO'] * df['P3']))) / beta
    df['SMI'] = df['SMI'].round(3)  # Arredonda o SMI para 3 casas decimais
    return df

# Mapeamento de riscos na tabela principal
def map_risks(df, risk_table):
    # Mapeia descrições de EE, SB e SO com base na tabela de riscos
    df = df.merge(risk_table[['Risco', 'EE']], left_on="EE", right_on="Risco").drop(columns=['Risco'])
    df = df.rename(columns={"EE_y": "EE_Desc"})
    
    df = df.merge(risk_table[['Risco', 'SB']], left_on="SB", right_on="Risco").drop(columns=['Risco'])
    df = df.rename(columns={"SB_y": "SB_Desc"})
    
    df = df.merge(risk_table[['Risco', 'SO']], left_on="SO", right_on="Risco").drop(columns=['Risco'])
    df = df.rename(columns={"SO_y": "SO_Desc"})
    
    return df

# Função principal para gerar a tabela final
def generate_table():
    # Lê os arquivos CSV
    relevancia, ee_data, sb_data, so_data, alunos_data, riscos_data = read_csv_files()

    # Une os dados dos arquivos EE, SB e SO
    combined_df = ee_data.merge(sb_data, on="ID").merge(so_data, on="ID")

    # Adiciona os nomes dos alunos com base no ID
    combined_df = combined_df.merge(alunos_data, on="ID")

    # Cria a tabela de riscos a partir do arquivo CSV
    risk_table = riscos_data

    # Calcula o SMI e adiciona os deltas
    combined_df = calculate_smi(combined_df, relevancia)

    # Adiciona descrições de riscos (EE, SB, SO)
    combined_df = map_risks(combined_df, risk_table)

    # Seleciona as colunas para a tabela final
    final_table = combined_df[["EE_x", "SB_x", "SO_x", "P1", "P2", "P3", "δ1", "δ2", "δ3", 
                               "Nome", "SMI", "EE_Desc", "SB_Desc", "SO_Desc"]]
    
    # Renomeia as colunas para remover o sufixo '_x'
    final_table = final_table.rename(columns={"EE_x": "EE", "SB_x": "SB", "SO_x": "SO", "EE_Desc": "EE", "SB_Desc": "SB", "SO_Desc": "SO"})

    # Classifica a tabela final de maneira decrescente pela coluna do SMI
    final_table = final_table.sort_values(by='SMI', ascending=False)

    # Retorna a tabela final
    return final_table

# Exporta a tabela final para um arquivo Excel
def main():
    final_table = generate_table()
    print(final_table)  # Exibe a tabela no console para verificação
    final_table.to_excel("saidas/Ranking_SMI_MMS-EDU.xlsx", index=False)  # Salva a tabela em um arquivo Excel

# Executa o script principal
if __name__ == "__main__":
    main()
