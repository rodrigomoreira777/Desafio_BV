WITH base AS (
  SELECT
    dados.ano AS ano,
    dados.sexo AS sexo,
    diretorio_cbo_2002.descricao AS cbo_2002_descricao
  FROM `basedosdados.br_me_caged.microdados_antigos` AS dados
  LEFT JOIN (
    SELECT DISTINCT cbo_2002, descricao
    FROM `basedosdados.br_bd_diretorios_brasil.cbo_2002`
  ) AS diretorio_cbo_2002
    ON dados.cbo_2002 = diretorio_cbo_2002.cbo_2002
  WHERE dados.ano BETWEEN 2015 AND 2019
)
SELECT 
  "COM_FILTRO" AS tipo, ano, sexo, COUNT(*) AS quantidade
FROM base
WHERE cbo_2002_descricao IN (
  {OCUPACOES}
)
GROUP BY ano, sexo
UNION ALL
SELECT 
  "SEM_FILTRO" AS tipo, ano, sexo, COUNT(*) AS quantidade
FROM base
GROUP BY ano, sexo
ORDER BY tipo, ano, sexo