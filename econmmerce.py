import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # Gráficos interativos
import streamlit as st  # 🎈 data web app desenvolvimento
import mysql.connector


@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])


@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


conn = init_connection()


def estadosLista(x, tabela):
    query = run_query(f"SELECT {x} FROM {tabela}")
    result = []
    for item in query:
        result.append(str(item)[2:-3])

    return result


def convertDf(x, y):
    df = pd.DataFrame(estadosLista(), columns=[x, y])
    return df

y = 'valorPedido'
x = st.sidebar.selectbox(
    "campos de consulta: ",
    ("categoria_produto", "tipo_pagamento", "estado_sigla", "cidade", "nota_avaliacao","data_de_compra", "ano_numero", "mes_texto", 'mes_numero', 'mes_numero_ano' ,'dia_semana' , 'dia_semana_numero'
,'semana_numero_ano', 'dia_numero_mes', 'dia_numero_ano', 'semana_nome', 'dia_ehdiautil', 'semestre_texto' , 'semestre_numero', 'semestre_numero_ano', 'trimestre_texto', 'trimestre_numero', 'trimestre_numero_ano'),
)
chaveTabela = 'key'
if x == "categoria_produto":
    tabela = "dimproduto"
    key = "dimProduto_key"
elif x == "nota_avaliacao":
    tabela = "dimavaliacao"
    key = "dimAvaliacao_key"
elif x == 'tipo_pagamento':
    tabela = 'dimpagamento'
    key = "dimPagamento_key"
elif x == 'cidade' or x == 'estado_sigla':
    tabela = 'dimlocalizacao'
    key = "dimLocalizacao_key"
elif x == 'data_de_compra' or x == 'ano_numero' or x == 'mes_texto' or x == 'mes_numero' or x == 'mes_numero_ano' or x == 'dia_semana' or x == 'dia_semana_numero' or x == 'semana_numero_ano' or x == 'dia_numero_mes' or x == 'dia_numero_ano' or x == 'semana_nome' or x == 'dia_ehdiautil' or x == 'semestre_texto' or x == 'semestre_numero' or x == 'semestre_numero_ano' or x == 'trimestre_texto' or x == 'trimestre_numero' or x == 'trimestre_numero_ano':
    tabela = 'dimtempo'
    key = "dimAtempo_key"
    chaveTabela = 'key_data'

def questao_1(x, y, tabela, key ,chaveTabela) :
    query =run_query(f"SELECT COUNT({y}) AS quantidade_pedido , dt.{x} from fatopedido fp LEFT JOIN {tabela} dt ON dt.{chaveTabela} = fp.{key} GROUP BY dt.dia_semana;") 
    result = []
    for item in query:
        result.append(str(item)[2:-3])
    return result




"""
-- 1) Qual a quantidade de pedidos realizados de acordo com os dias da semana ou final de semana?
"""

st.write(questao_1(x,y,tabela,key, chaveTabela))
