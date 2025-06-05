# 💼 Linha de Crédito Inclusiva — Banco BV

Este projeto estrutura uma linha de crédito proposta ao Banco BV com juros reduzidos para empresas que contratarem ou alocarem **mulheres em cargos técnicos**, como os de tecnologia, engenharia ou P&D.

## 🎯 Objetivo

Demonstrar com dados públicos a desigualdade de gênero nesses setores e propor um modelo de incentivo com base em evidências.

## Panorama populacional entre homens e mulheres

Ao analisarmos a população brasileira entre 15 e 65 anos — considerada como economicamente ativa — nos últimos anos, observamos uma distribuição relativamente equilibrada entre homens e mulheres.

A tabela abaixo resume essa distribuição no período de 2015 a 2019:

| Ano  | Homens       | Mulheres     | Total Geral   | Proporção Homens | Proporção Mulheres |
|------|--------------|--------------|---------------|------------------|--------------------|
| 2015 | 68.896.752   | 72.358.621   | 141.255.373   | 48,77%           | 51,23%             |
| 2016 | 69.531.432   | 72.987.056   | 142.518.488   | 48,79%           | 51,21%             |
| 2017 | 70.089.786   | 73.528.157   | 143.617.943   | 48,80%           | 51,20%             |
| 2018 | 70.580.163   | 73.986.466   | 144.566.629   | 48,82%           | 51,18%             |
| 2019 | 71.075.097   | 74.436.176   | 145.511.273   | 48,85%           | 51,15%             |

**Fonte dos dados:**  
- **Base:** Projeção populacional por sexo e idade simples (IBGE).  
- **Arquivo bruto:** `dados/brutos/projecoes_2024_tab1_idade_simples.xlsx`
- **Arquivo processado:** `dados/tratados/projecoes_reestruturadas.xlsx`
- **Script de processamento:** `executar_analises_bv.py`  
- **Transformações aplicadas:**
  - Seleção da faixa etária entre 15 e 65 anos.
  - Agrupamento por ano e sexo.
  - Cálculo do total geral e proporção percentual por gênero.

## Participação de mulheres em áreas técnicas

Entretanto, ao analisarmos a distribuição de vínculos empregatícios em áreas como **Engenharia**, **Tecnologia da Informação** e **Pesquisa & Desenvolvimento**, observamos uma predominância significativa de homens ao longo dos últimos anos.

A tabela a seguir demonstra esse desequilíbrio:

| Área             | Ano  | Homens  | Mulheres | Total Geral | Proporção Homens | Proporção Mulheres |
|------------------|------|---------|----------|--------------|------------------|--------------------|
| Eng., Tec. e P&D | 2015 | 204.156 | 105.424  | 309.580      | 66%              | 34%                |
| Eng., Tec. e P&D | 2016 | 183.432 |  93.017  | 276.449      | 66%              | 34%                |
| Eng., Tec. e P&D | 2017 | 189.289 |  95.298  | 284.587      | 67%              | 33%                |
| Eng., Tec. e P&D | 2018 | 218.537 | 112.069  | 330.606      | 66%              | 34%                |
| Eng., Tec. e P&D | 2019 | 244.534 | 122.037  | 366.571      | 67%              | 33%                |

**Fonte dos dados:**  
- **Base:** Microdados do CAGED (2015–2019) — [Base dos Dados](https://basedosdados.org)
- **Arquivo processado:** `dados/tratados/quantidade_vinculos_por_genero_comparativo.xlsx`
- **Script:** `executar_analises_bv.py`
- **Profissões consideradas técnicas:** estão listadas no arquivo `ocupacoes_tecnicas.txt` na raiz do projeto.

Essas ocupações incluem engenheiros (diversas especialidades), desenvolvedores de sistemas, gerentes de P&D, professores de engenharia, pesquisadores e técnicos em tecnologia da informação, entre outros.



## 📁 Estrutura

```
bv-linha-de-credito-inclusiva/
├── ocupacoes_tecnicas.txt
├── sql/
│ ├── 01_todos_vinculos.sql
│ ├── 02_exclusao_ocupacoes.sql
│ ├── 03_media_salarial.sql
│ └── 04_quantidade_vinculos.sql
├── dados/
│ ├── brutos/
│ └── tratados/
├── executar_analises_bv.py
└── requirements.txt

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
