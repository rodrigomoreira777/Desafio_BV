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

## Diferença salarial entre áreas técnicas e demais profissões

Além da baixa representatividade feminina nas áreas técnicas, outro ponto relevante é a **diferença salarial expressiva** entre essas áreas e a média geral das demais ocupações.

A tabela abaixo apresenta a comparação entre a média salarial das profissões técnicas (Engenharia, Tecnologia da Informação e P&D) e a média salarial geral de todas as ocupações no Brasil, com base nos vínculos registrados entre 2015 e 2019:

| Ano  | Eng., Tec. e P&D (R$) | Geral - todas (R$) | Diferença (%) |
|------|------------------------|---------------------|----------------|
| 2015 | 4.049,60               | 1.321,57            | 306%           |
| 2016 | 4.239,42               | 1.444,44            | 293%           |
| 2017 | 4.307,31               | 1.537,83            | 280%           |
| 2018 | 4.205,04               | 1.567,81            | 268%           |
| 2019 | 4.486,47               | 1.634,84            | 274%           |
| **Média Geral** | **4.257,57** | **1.501,29**        | **284%**       |

**Fonte dos dados:**  
- **Base:** Microdados do CAGED (2015–2019) — [Base dos Dados](https://basedosdados.org)  
- **Arquivo processado:** `dados/tratados/media_salarial_por_genero_comparativo.xlsx`  
- **Script:** `executar_analises_bv.py`  
- **Filtro técnico aplicado:** ocupações listadas em `ocupacoes_tecnicas.txt`

A média salarial nas áreas técnicas é, consistentemente, **2,8 vezes maior** do que a média de todas as ocupações. Isso reforça a importância de promover a equidade de gênero nessas áreas, que concentram não apenas maior qualificação, mas também os melhores salários.

## Proposta de crédito com incentivo à inclusão

Com base nos dados apresentados, torna-se evidente que:

- A população brasileira entre homens e mulheres é equilibrada;
- Mulheres estão sub-representadas em áreas de maior qualificação e remuneração;
- Essas áreas concentram parte significativa da renda média formal no país.

Diante disso, propõe-se a criação de uma **linha de crédito diferenciada pelo Banco BV**, voltada para empresas que **assumirem o compromisso de contratar ou realocar mulheres** em cargos técnicos — como engenharia, tecnologia da informação e pesquisa & desenvolvimento.

### Mecanismo proposto

A empresa interessada submete um **pleito formal de contratação** diretamente na plataforma do Banco BV, por meio de um formulário simplificado (inspirado nos simuladores já utilizados pelo banco).

Nesse formulário, a empresa deverá informar:

- Número de mulheres contratadas ou realocadas nas ocupações técnicas;
- Quadro de pessoal atual e projetado;
- CNAE e setor de atuação;
- CNPJ e demais dados cadastrais.

Com base nesses dados, será calculada uma **pontuação de inclusão** que determinará:

- Redução progressiva da taxa de juros;
- Possibilidade de carência no início do pagamento;
- Outras condições facilitadas de financiamento.

Essa proposta visa alinhar objetivos sociais e econômicos, **incentivando a equidade de gênero nas áreas mais estratégicas** do mercado de trabalho.

---

**Exemplo de interface de submissão:**

O formulário pode seguir o mesmo padrão visual do simulador de financiamento de veículos já disponível no site do BV, adaptado para o contexto de pleito empresarial:

> Etapas:
> 1. Dados da empresa
> 2. Informações de inclusão (contratações/recolocações)
> 3. Dados financeiros
> 4. Simulação do crédito com benefícios aplicáveis

---

*A implementação poderá evoluir para um portal de acompanhamento de indicadores, com integração a dados do eSocial ou RAIS para validação automática das contratações declaradas.*

## Simulador de crédito com incentivo à inclusão

Inspirado no fluxo de simulação já utilizado pelo Banco BV (como no crédito para veículos), a proposta prevê a criação de um **simulador de crédito com contrapartida social** no próprio site da instituição, com etapas objetivas e guiadas.

### Etapas da simulação

O formulário de pleito empresarial seria dividido em quatro etapas simples:

**1. Dados da empresa**
- Razão social
- CNPJ
- CNAE principal
- Faturamento bruto anual
- Setor de atuação

**2. Compromisso de inclusão**
- Número de mulheres a serem contratadas ou realocadas nas áreas técnicas
- Profissões alvo (selecionadas a partir da lista de ocupações técnicas)
- Percentual de mulheres no quadro atual vs. projetado

**3. Condições do crédito**
- Valor solicitado
- Prazo desejado (em meses)
- Necessidade de carência

**4. Simulação e benefícios**
- Simulação do crédito com:
  - Taxa de juros padrão (sem inclusão)
  - Taxa reduzida com base no índice de inclusão
  - Benefícios aplicáveis (ex: carência, prazo ampliado)
- Resultado exibido de forma comparativa

---

### 🏢 Exemplo prático: Empresa X

**Cenário:**
- Empresa fictícia do setor de tecnologia
- CNPJ: 00.000.000/0001-00
- Solicita um crédito de **R$ 500.000** com pagamento em **36 meses**
- Compromete-se a contratar **5 mulheres desenvolvedoras** nos próximos 6 meses

**Resultado da simulação:**

| Condição                         | Crédito padrão (mercado) | Crédito com inclusão |
|----------------------------------|---------------------------|-----------------------|
| Taxa de juros mensal             | 2,10%                     | **1,45%**             |
| Taxa anual (CET estimada)        | ~28%                      | **~18,8%**            |
| Valor total ao final             | R$ 760.000                | **R$ 648.000**        |
| Economia potencial               | –                         | **R$ 112.000**        |
| Carência                         | Não                       | **Sim (3 meses)**     |
| Liberação de recursos            | Após análise              | Após análise (prioridade)

**Fontes de referência para taxas de crédito empresarial**:
- Taxas médias de mercado: [Banco Central do Brasil](https://www.bcb.gov.br/estatisticas/taxasjuros)
- Estimativas de CET para PJ com e sem garantias

---

### Impacto

Esse modelo de crédito beneficia diretamente empresas que buscam expandir sua força de trabalho de forma mais inclusiva, sem necessidade de renúncia fiscal por parte do Estado. Ao mesmo tempo, melhora a imagem institucional do banco, gera impacto social positivo mensurável e utiliza a própria infraestrutura digital já existente no site do BV.

---

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
