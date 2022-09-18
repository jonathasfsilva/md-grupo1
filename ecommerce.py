from curses import color_pair
from operator import xor
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # Gráficos interativos
import streamlit as st  # 🎈 data web app desenvolvimento
#from graficos import *

#Comando de execução do streamlit
st.set_page_config(
    page_title="Dashboard E-commerce Olist",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded")

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

# Organizando graficos lado a lado por meio de colunas
placeholder = st.empty() # criando um  container para as metricas
with placeholder.container():
    kpi1, kpi2, kpi3 = st.columns(3)
    fig_col1, fig_col2 = st.columns(2)
    fig_col3, fig_col4 = st.columns(2)
    fig_col5, fig_col6= st.columns(2)

#Metricas e indicadores
def metrica1(kpi1,value,delta,label):
    metrica1 = kpi1.metric(
            label1=label,
            value = value,
            delta = delta,)
    return metrica1 

def metrica2(kpi2,value,delta,label):
    metrica2 = kpi2.metric(
            label2=label,
            value=value,
            delta=delta,)
    return metrica2

def metrica3(kpi3,value,delta,label):
    metrica3 = kpi3.metric(
    label3=label,
            value=value,
            delta=delta,)
    return metrica3

#Graficos
def density_heatmap(fig_col1,df,x,y):
    with fig_col1:
        st.markdown("### Density Heatmap")
        fig = px.density_heatmap(df, y, x)
        return st.write(fig)

def histogram(fig_col2,df,x,y):  
    with fig_col2:
        st.markdown("###  Histogram")
        fig2 = px.histogram(df,x,y)
        return st.write(fig2)

def bar_chart(fig_col3,df, x,y,color):
    with fig_col3:
        st.markdown("###  Bar Chart")
        fig3 =  px.bar(df, y, x) 
        return st.write(fig3)

def  scatter_chart(fig_col4, df ,x, y):   
    with fig_col4:
        st.markdown("### Scatter Chart")
        fig4 =  px.scatter(df, y, x) 
        return st.write(fig4)

def line_chart(fig_col5, df ,x,y):
    with fig_col5:
        st.markdown("### line Chart")
        fig5 = px.line(df, y)
        return st.write(fig5)

def pie_chart(fig_col6, df ,x, y):
    with fig_col6:
        st.markdown("###  Pie Chart")
        fig6 = px.pie(df, values=y, names=x)
        return st.write(fig6)

def box_chart(df,x,y):
    st.markdown("### Box Chart")
    fig7 = px.box(df, x=x,y=y)
    return st.write(fig7)
    
#Condições dos Filtros
if opcoes_arq == 'Pedidos por dia da semana':
    df = pd.DataFrame(questao1)
    #Definição das variaveis 
    x = df["dia_semana"]
    y = df["quantidade_pedido"]
    #Chamada dos gráficos
    density_heatmap(fig_col1,df,x,y)
    histogram(fig_col2,df,x,y)
    bar_chart(fig_col3,df, x,y,None)
    scatter_chart(fig_col4, df ,x, y)
    #Exibindo df
    st.markdown('## View Dataframe')
    st.write('Quantidade de pedidos realizados de acordo com os dias da semana ou final de semana')
    st.dataframe(df)

elif opcoes_arq == 'Pedidos em datas comemorativas':
    df = pd.DataFrame(questao2)
    #Definição das variaveis 
    y = df["dia_mes"]
    x = df["quantidade_pedido"]
    color = df["dia_ehdiautil"]
    #Chamada dos gráficos
    density_heatmap(fig_col1,df,x,y)
    histogram(fig_col2,df,x,y)
    scatter_chart(fig_col3, df ,x, y)
    line_chart(fig_col4, df,x,y)
    #Exibindo df
    st.markdown('## View Dataframe')
    st.write('Períodos que ocorrem maior quantidade de pedidos que estão relacionados a datas comemorativas')
    st.dataframe(df)

elif opcoes_arq == 'Avaliação dos produtos por categorias':
    df = pd.DataFrame(questao3)
    #Definição das variaveis 
    x = df["quantidade_pedido"]
    y = df["media_nota_avaliacao"]
    color = df["categoria_produto"]
    #Chamada dos gráficos
    histogram(fig_col1,df,x,color)
    bar_chart(fig_col2,df, y,color,None)
    scatter_chart(fig_col3, df ,x, y)
    density_heatmap(fig_col4,df,color,x)
    #Exibindo df
    st.markdown('## View Dataframe')
    st.write('Média de avaliação dos pedidos por categoria de produto')
    st.dataframe(df)

elif opcoes_arq == 'Forma de pagamento do pedido por estado':
    df = pd.DataFrame(questao4)
    #Definição das variaveis 
    x = df["quantidade_pedido"]
    y = df["estado_sigla"]
    color = df["tipo_pagamento"]
    #Chamada dos gráficos
    density_heatmap(fig_col1,df,x,y)
    histogram(fig_col2,df,y,x)
    bar_chart(fig_col3,df,color,y,x)
    scatter_chart(fig_col4, df ,x, y)
    pie_chart(fig_col5, df , color,x)
    #Exibindo df
    st.markdown('## View Dataframe')
    st.write('Quantidade de pedidos em relação a forma de pagamento por estado ')
    st.dataframe(df)

elif opcoes_arq == 'Categoria do pedido por estação do ano':
    df = pd.DataFrame(questao5)
    #Definição das variaveis 
    x = df["quantidade_pedido"]
    y = df["categoria_produto"]
    color = df["estacoe"]
    #Chamada dos gráficos
    density_heatmap(fig_col1,df,x,y)
    pie_chart(fig_col2, df , color,x)
    histogram(fig_col3,df,color,x)
    scatter_chart(fig_col4, df ,x, y)
    #Exibindo df
    st.markdown('## View Dataframe')
    st.write('Quantidade de  categorias de pedido  por estação do ano')
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