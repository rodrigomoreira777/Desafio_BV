# 💼 Linha de Crédito Inclusiva — Banco BV

Este projeto estrutura uma linha de crédito proposta ao Banco BV com juros reduzidos para empresas que contratarem ou alocarem **mulheres em cargos técnicos**, como os de tecnologia, engenharia ou P&D.

## 🎯 Objetivo

Demonstrar com dados públicos a desigualdade de gênero nesses setores e propor um modelo de incentivo com base em evidências.

## 🧩 Premissas

1. As áreas técnicas apresentam **baixa participação feminina**.
2. Há **diferença salarial média por gênero** mesmo nessas ocupações.
3. A proposta vincula **maior inclusão de mulheres** a **menores taxas de juros**.

## 📁 Estrutura

```
bv-linha-de-credito-inclusiva/
├── scripts/
│   └── ocupacoes_tecnicas.txt
├── sql/
│   ├── 01_todos_vinculos.sql
│   ├── 02_exclusao_ocupacoes.sql
│   ├── 03_media_salarial.sql
│   └── 04_quantidade_vinculos.sql
├── dados/
│   ├── brutos/
│   └── tratados/
├── executar_analises_bv.py
└── requirements.txt
```

## 🚀 Como usar

1. Configure sua chave do Google BigQuery (`.json`)
2. Edite `executar_analises_bv.py` com o caminho da chave e `project_id`
3. Instale dependências:
```bash
pip install -r requirements.txt
```
4. Execute o script:
```bash
python executar_analises_bv.py
```

## 📊 Fontes de Dados

- [Base dos Dados - CAGED](https://basedosdados.org)
- [IBGE - Projeções Populacionais](https://www.ibge.gov.br)

## 📄 Licença

MIT License
