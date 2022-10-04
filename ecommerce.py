
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
    query = run_query(
""" SELECT 
        COUNT({y}) AS quantidade_pedido  
        , t.{x} 
        , dt.dia_semana
    FROM fatopedido fp 
    LEFT JOIN {tabela} t ON t.{chaveTabela} = fp.{key} 
    LEFT JOIN dimtempo dt ON dt.key_data = fp.dimATempo_key
    GROUP BY 3,2
    ORDER BY 1 DESC;
""".format(
    x=x,
    y=y,
    tabela=tabela,
    chaveTabela=chaveTabela,
    key=key
)) 
    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))
    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido',x,'dia_semana'])
    return st.write(df)


def questao_2(x, y, tabela, key ,chaveTabela) :
    query = run_query(
""" SELECT 
        COUNT(fp.{y}) AS quantidade_pedido
        , t.{x} 
        , dt.dia_ehdiautil
    FROM fatopedido fp
    LEFT JOIN {tabela} t ON t.{chaveTabela} = fp.{key} 
    LEFT JOIN dimtempo dt ON dt.key_data = fp.dimATempo_key
    GROUP BY 2
    ORDER BY 1 DESC;
""".format(
    x=x,
    y=y,
    tabela=tabela,
    chaveTabela=chaveTabela,
    key=key
)) 
 
    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))
    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido',x,'dia_ehdiautil'])
    return st.write(df)
    
    
def questao_3(x, y, tabela, key, chaveTabela) :
    query = run_query(
""" SELECT 
        COUNT(fp.{y}) AS quantidade_pedido
        , ROUND(AVG(da.nota_avaliacao),2) AS media_nota_avaliacao
        , dp.{x}
    FROM fatopedido fp
    LEFT JOIN dimavaliacao da ON da.key = fp.dimAvaliacao_key
    LEFT JOIN {tabela} dp ON dp.{chaveTabela} = fp.{key}
    GROUP BY 3
    ORDER BY 1 DESC;
""".format(
    x=x,
    y=y,
    tabela=tabela,
    chaveTabela=chaveTabela,
    key=key
)) 

    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))
    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido',x,'media_nota_avaliacao'])    
    return st.write(df)
    

def questao_4(x, y, tabela, key, chaveTabela) :
    query = run_query(
    """ SELECT 
            COUNT(fp.{y}) AS quantidade_pedido
            , dl.estado_sigla
            , dp.{x}
        FROM fatopedido fp
        LEFT JOIN dimlocalizacao dl ON dl.key = fp.dimLocalizacao_key
        LEFT JOIN {tabela} dp ON dp.{chaveTabela} = fp.{key}
        GROUP BY 3
        ORDER BY 1 DESC;
    """.format(
        x=x,
        y=y,
        tabela=tabela,
        chaveTabela=chaveTabela,
        key=key
)) 

    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))
    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido',  'estado_sigla', x])    
    st.write(df)
    st.markdown("###  Bar Chart")

    fig4 =  px.bar(df,x='estado_sigla',y='quantidade_pedido', color=x) 
    st.write(fig4)

    fig41 =  px.scatter(df,x='estado_sigla' ,y= 'quantidade_pedido', color= x) 
    st.write(fig41)


def questao_5(x, y, tabela, key, chaveTabela) :
    query = run_query(
    """ 
    SELECT 
        COUNT(fp.{y}) AS quantidade_pedido
        , dp.{x}
        , CASE 
            WHEN DATE_FORMAT(data_de_compra, "%d/%m") >= '20/03' AND DATE_FORMAT(data_de_compra, "%d/%m") < '20/06'  THEN 'outono'
            WHEN DATE_FORMAT(data_de_compra, "%d/%m") >= '20/06' AND DATE_FORMAT(data_de_compra, "%d/%m") < '22/09'  THEN 'inverno'
            WHEN DATE_FORMAT(data_de_compra, "%d/%m") >= '22/09' AND DATE_FORMAT(data_de_compra, "%d/%m") < '21/12'  THEN 'primavera'
            ELSE 'verão' 
        END AS estacoes
    FROM fatopedido fp
    LEFT JOIN {tabela} dp ON dp.{chaveTabela} = fp.{key}
    LEFT JOIN dimtempo dt ON dt.key_data = fp.dimATempo_key
    GROUP BY 2, 3
    ORDER BY 1 DESC
    """.format(
        x=x,
        y=y,
        tabela=tabela,
        chaveTabela=chaveTabela,
        key=key
)) 

    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))
    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido',x,'estações'])    
    return st.write(df)
    

st.write(questao_1(x,y,tabela,key, chaveTabela))
st.write(questao_2(x,y,tabela,key, chaveTabela))
st.write(questao_3(x,y,tabela,key, chaveTabela))
st.write(questao_4(x,y,tabela,key, chaveTabela))
st.write(questao_5(x,y,tabela,key, chaveTabela))


    

