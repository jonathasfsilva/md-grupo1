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


tabela = ""

x = st.sidebar.selectbox(
    "campos de consulta: ",
    ("categoria_produto", "tipo_pagamento", "estado_sigla", "cidade", "nota_avaliacao"),
)
if x == "categoria_produto":
    tabela = "dimproduto"
elif x == "nota_avaliacao":
    tabela = "dimavaliacao"
elif x == 'tipo_pagamento':
    tabela = 'dimlocalizacao'


"""
-- 1) Qual a quantidade de pedidos realizados de acordo com os dias da semana ou final de semana?
SELECT 
	COUNT(fp.valorPedido) AS quantidade_pedido
    , dt.dia_semana
FROM fatopedido fp
LEFT JOIN dimtempo dt ON dt.key_data = fp.dimTempo_key_data
GROUP BY dt.dia_semana;
"""

st.write(estadosLista(x, tabela))
