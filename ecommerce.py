#import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from graficos import *

# read csv from DW
questao1 = pd.read_csv('data/questao_1.csv')
questao2 = pd.read_csv('data/questao_2.csv')
questao3 = pd.read_csv('data/questao_3.csv')
questao4 = pd.read_csv('data/questao_4.csv')
questao5 = pd.read_csv('data/questao_5.csv')

# dashboard title
st.title("Dashboard E-commerce Olist")
st.subheader('Este projeto apresenta o resultado da modelagem do DW gerado por meio dos dados publico de E-commerce Olist com foco de estudo nos Pedidos.')

# Opções dos filtros
with st.sidebar:
    st.header('Modelagem de Dados - Grupo 1')
    opcoes_arq = st.selectbox("Opções de Consultas:",('Pedidos em datas comemorativas','Pedidos por dia da semana','Avaliação dos produtos por categorias','Forma de pagamento do pedido por estado','Categoria do pedido por estação do ano'))
    
#Condições dos Filtros
if opcoes_arq == 'Pedidos por dia da semana':
    st.write('Quantidade de pedidos realizados de acordo com os dias da semana ou final de semana')
    df = pd.DataFrame(questao1)
   
    #Definição das variaveis 
    x = df["dia_semana"]
    y = df["quantidade_pedido"]
    
    #Chamada dos gráficos
    density_heatmap(fig_col1,df,x,y)
    histogram(fig_col2,df,x,y)
    bar_chart(fig_col3,df, x,y)
    scatter_chart(fig_col4, df ,x, y)
    line_chart(fig_col5, df ,x)
    pie_chart(fig_col6, df ,x, y)
    box_chart(df,x,y)

    st.markdown('## View Dataframe')
    st.dataframe(df)
elif opcoes_arq == 'Pedidos em datas comemorativas':
    st.write('Períodos que ocorrem maior quantidade de pedidos que estão relacionados a datas comemorativas')
    df = pd.DataFrame(questao2)
    st.markdown('## View Dataframe')
    st.dataframe(df)
elif opcoes_arq == 'Avaliação dos produtos por categorias':
    st.write('Média de avaliação dos pedidos por categoria de produto')
    df = pd.DataFrame(questao3)
    st.markdown('## View Dataframe')
    st.dataframe(df)
elif opcoes_arq == 'Forma de pagamento do pedido por estado':
    st.write('Quantidade de pedidos em relação a forma de pagamento por estado ')
    df = pd.DataFrame(questao4)
    st.markdown('## View Dataframe')
    st.dataframe(df)
elif opcoes_arq == 'Categoria do pedido por estação do ano':
    st.write('Quantidade de  categorias de pedido  por estação do ano')
    df = pd.DataFrame(questao5)
    st.markdown('## View Dataframe')
    st.dataframe(df)
else:
    st.write('Nada foi carregado, por favor selecione umas das opções presente no sidebar')

def metrcia1_construcao():
    ''' 
    df['quantidade_pedido'] =df['quantidade_pedido'].astype(int)

    df["ped_qtd_new"] = df["quantidade_pedido"] * np.random.choice(range(1, 5))
    df["dia_semana_new"] = df["dia_semana"] * np.random.choice(range(1, 5))
    avg_qtd_pedido= np.mean(df["ped_qtd_new"])
    count_pedido = int(df["ped_qtd_new"]).count + np.random.choice(range(1, 30))
    balance= np.mean(df["ped_qtd_new"])

    #Calculo para a metrica1
    label1 = "Data de compra ⏳"
    value1 = round(avg_qtd_pedido)
    delta1 = round(avg_qtd_pedido) -10
    #Calculo para a metrica2
    label2="Categorias dos produtos 💍",
    value2 = int(count_pedido),
    delta2 =-10 + count_pedido,
    #Calculo para a metrica3
    label3="Valor  dos Pedidos ＄"
    value3 = f"$ {round(balance,2)} ",
    delta3 = -round(balance / count_pedido) * 100,
    #Chamada das metricas
    #metrica1(kpi1,value1,delta1,label1)
    #metrica2(kpi2,value2,delta2,label2)
    #metrica3(kpi3,value3,delta3,label3)'''
    return('Esta dando erro de tipagem')