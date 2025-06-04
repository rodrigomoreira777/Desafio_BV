SELECT
  dados.ano AS ano,
  diretorio_cbo_2002.descricao AS cbo_2002_descricao,
  dados.grau_instrucao AS grau_instrucao,
  dados.sexo AS sexo,
  COUNT(*) AS quantidade
FROM `basedosdados.br_me_caged.microdados_antigos` AS dados
LEFT JOIN (
  SELECT DISTINCT cbo_2002, descricao
  FROM `basedosdados.br_bd_diretorios_brasil.cbo_2002`
) AS diretorio_cbo_2002
  ON dados.cbo_2002 = diretorio_cbo_2002.cbo_2002
WHERE dados.ano BETWEEN 2015 AND 2019
GROUP BY
  dados.ano, diretorio_cbo_2002.descricao, dados.grau_instrucao, dados.sexo
ORDER BY
  dados.ano, diretorio_cbo_2002.descricao