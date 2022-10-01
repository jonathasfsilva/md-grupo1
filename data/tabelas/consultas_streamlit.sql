-- 1) Qual a quantidade de pedidos realizados de acordo com os dias da semana ou final de semana?
SELECT 
	COUNT(fp.valorPedido) AS quantidade_pedido
    , dt.dia_semana
FROM fatopedido fp
LEFT JOIN dimtempo dt ON dt.key_data = fp.dimATempo_key
GROUP BY 2;

-- 2) Os períodos que ocorrem maior quantidade vendas estão relacionados a datas comemorativas?
SELECT 
	COUNT(fp.valorPedido) AS quantidade_pedido
    , CONCAT(DATE_FORMAT(data_de_compra, '%d'),'/', DATE_FORMAT(data_de_compra, '%m')) AS dia_mes
    , dt.dia_ehdiautil
FROM fatopedido fp
LEFT JOIN dimtempo dt ON dt.key_data = fp.dimATempo_key
GROUP BY 2, 3
ORDER BY 1 DESC;

-- 3) Qual a média de avaliação dos pedidos por categoria de produto?
SELECT 
	COUNT(fp.valorPedido) AS quantidade_pedido
    , ROUND(AVG(da.nota_avaliacao),2) AS media_nota_avaliacao
    , dp.categoria_produto
FROM fatopedido fp
LEFT JOIN dimavaliacao da ON da.key = fp.dimAvaliacao_key
LEFT JOIN dimproduto dp ON dp.key = fp.dimProduto_key
GROUP BY 3
ORDER BY 1 DESC;

-- 4) Qual a quantidade de pedidos em relação aos seu tipo de pagamento por estado ?
SELECT 
	COUNT(fp.valorPedido) AS quantidade_pedido
    , dl.estado_sigla
    , dp.tipo_pagamento
FROM fatopedido fp
LEFT JOIN dimlocalizacao dl ON dl.key = fp.dimLocalizacao_key
LEFT JOIN dimpagamento dp ON dp.key = fp.dimPagamento_key
GROUP BY 2, 3
ORDER BY 1 DESC;

-- 5) Quantidade de  categorias de pedido  vendidas por estação do ano? 
SELECT 
	COUNT(fp.valorPedido) AS quantidade_pedido
	, dp.categoria_produto
    , CASE 
		 WHEN DATE_FORMAT(data_de_compra, "%d/%m") >= '20/03' AND DATE_FORMAT(data_de_compra, "%d/%m") < '20/06'  THEN 'outono'
		 WHEN DATE_FORMAT(data_de_compra, "%d/%m") >= '20/06' AND DATE_FORMAT(data_de_compra, "%d/%m") < '22/09'  THEN 'inverno'
         WHEN DATE_FORMAT(data_de_compra, "%d/%m") >= '22/09' AND DATE_FORMAT(data_de_compra, "%d/%m") < '21/12'  THEN 'primavera'
     ELSE 'verão' END AS estacoes
FROM fatopedido fp
LEFT JOIN dimproduto dp ON dp.key = fp.dimProduto_key
LEFT JOIN dimtempo dt ON dt.key_data = fp.dimATempo_key
GROUP BY 2, 3
ORDER BY 1 DESC