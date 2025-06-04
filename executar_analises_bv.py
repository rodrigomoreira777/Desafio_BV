# Projeto: Linha de Crédito Inclusiva - Banco BV

import os
import pandas as pd
from basedosdados import read_sql

# ================================
# 🔧 Configurações Iniciais
# ================================
# **Não compartilhado**
CREDENTIALS_PATH = "CAMINHO/DA/SUA/CHAVE.json"
BILLING_PROJECT_ID = "SEU_PROJECT_ID"
# **Não compartilhado**
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH

# ================================
# 📥 Funções auxiliares
# ================================
def carregar_ocupacoes(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        ocupacoes = [linha.strip() for linha in f if linha.strip()]
    return ",\n    ".join([f"'{o}'" for o in ocupacoes])

def carregar_query(nome_arquivo):
    with open(f"sql/{nome_arquivo}", "r", encoding="utf-8") as f:
        return f.read()

def executar_query(query: str, nome_arquivo: str):
    df = read_sql(query, billing_project_id=BILLING_PROJECT_ID)
    df.to_excel(f"dados/tratados/{nome_arquivo}.xlsx", index=False)
    print(f"✅ Resultado salvo em: dados/tratados/{nome_arquivo}.xlsx")

# ================================
# 🚀 Execução Principal
# ================================
if __name__ == "__main__":
    # Carregar ocupações técnicas
    ocupacoes_sql = carregar_ocupacoes("scripts/ocupacoes_tecnicas.txt")

    # Lista de (arquivo_sql, nome_arquivo_saida)
    tarefas = [
        ("01_todos_vinculos.sql", "agrupado_caged_simples"),
        ("02_exclusao_ocupacoes.sql", "agrupado_sem_ocupacoes_excluidas"),
        ("03_media_salarial.sql", "media_salarial_por_genero"),
        ("04_quantidade_vinculos.sql", "quantidade_vinculos_por_genero")
    ]

    for sql_file, output_name in tarefas:
        query = carregar_query(sql_file).replace("{OCUPACOES}", ocupacoes_sql)
        executar_query(query, output_name)

    # Manipular planilha do IBGE
    IBGE_ARQUIVO = "dados/brutos/projecoes_2024_tab1_idade_simples.xlsx"
    df_ibge = pd.read_excel(IBGE_ARQUIVO, sheet_name="1) POP_IDADE SIMPLES")
    df_long = pd.melt(df_ibge, id_vars=["IDADE", "SEXO", "LOCAL"], var_name="ANO", value_name="POPULACAO")
    df_long.to_excel("dados/tratados/projecoes_reestruturadas.xlsx", index=False)
    print("✅ IBGE tratado salvo em: dados/tratados/projecoes_reestruturadas.xlsx")
