#import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Dashboard E-commerce Olist",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

# read csv from DW
questao1 = pd.read_csv('data/questao_1.csv')
questao2 = pd.read_csv('data/questao_2.csv')
questao3 = pd.read_csv('data/questao_3.csv')
questao4 = pd.read_csv('data/questao_4.csv')
questao5 = pd.read_csv('data/questao_5.csv')

# dashboard title
st.title("Dashboard E-commerce Olist")
st.subheader('Este projeto apresenta o resultado da modelagem do DW em relação aos Pedidos.')

# Opções dos filtros
with st.sidebar:
    st.header('Modelagem de Dados - Grupo 1')
    opcoes_arq = st.selectbox("Opções de Consultas:",('Pedidos em datas comemorativas','Pedidos por dia da semana','Avaliação dos produtos por categorias','Forma de pagamento do pedido por estado','Categoria do pedido por estação do ano'))
    
#Condições dos Filtros
if opcoes_arq == 'Pedidos por dia da semana':
    st.write('Quantidade de pedidos realizados de acordo com os dias da semana ou final de semana')
    df = pd.DataFrame(questao1)
    st.dataframe(questao1)
elif opcoes_arq == 'Pedidos em datas comemorativas':
    st.write('Períodos que ocorrem maior quantidade de pedidos que estão relacionados a datas comemorativas')
    df = pd.DataFrame(questao2)
    st.dataframe(questao2)
elif opcoes_arq == 'Avaliação dos produtos por categorias':
    st.write('Média de avaliação dos pedidos por categoria de produto')
    df = pd.DataFrame(questao3)
    st.dataframe(questao3)
elif opcoes_arq == 'Forma de pagamento do pedido por estado':
    st.write('Quantidade de pedidos em relação a forma de pagamento por estado ')
    df = pd.DataFrame(questao4)
    st.dataframe(questao4)
elif opcoes_arq == 'Categoria do pedido por estação do ano':
    st.write('Quantidade de  categorias de pedido  por estação do ano')
    df = pd.DataFrame(questao5)
    st.dataframe(questao5)

#falta organizar essa parte pra pegar as colunas queserão passadas pra cada grafico com a seleção dos filtros
# dataframe filter
#df = df[df["job"] == job_filter]
#df["age_new"] = df["age"] * np.random.choice(range(1, 5))
#df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))
# creating KPIs
#avg_age = np.mean(df["age_new"])
#count_married = int(df[(df["marital"] == "married")]["marital"].count()+ np.random.choice(range(1, 30)))
#balance = np.mean(df["balance_new"])

#Informações a serem passada para os gráficos 
#x
#y

# Organizando graficos lado a lado por meio de colunas
placeholder = st.empty() # crinado um  container para as metricas
with placeholder.container():
    kpi1, kpi2, kpi3 = st.columns(3)
    fig_col1, fig_col2 = st.columns(2)
    fig_col3, fig_col4 = st.columns(2)
    fig_col5, fig_col6= st.columns(2)

def metricas(kpi1, kpi2, kpi3):
        metrica1 = kpi1.metric(
            label="Data de compra ⏳",
            #value=round(avg_age),
            #delta=round(avg_age) - 10,
        )
        
        metrica2 = kpi2.metric(
            label="Categorias dos produtos 💍",
            #value=int(count_married),
            #delta=-10 + count_married,
        )
        
        metrica3 = kpi3.metric(
            label="Valor  dos Pedidos ＄",
            #value=f"$ {round(balance,2)} ",
            #delta=-round(balance / count_married) * 100,
        )
        return(metrica1,metrica2,metrica3)
    
#Graficos
def density_heatmap(fig_col1,df,x,y):
    with fig_col1:
        st.markdown("### Density Heatmap")
        fig = px.density_heatmap(df, y, x)
        return st.write(fig)

def histogram(fig_col2,df,x):  
    with fig_col2:
        st.markdown("###  Histogram")
        fig2 = px.histogram(df,x)
        return st.write(fig2)

def bar_chart(fig_col3,df, x,y):
    with fig_col3:
        st.markdown("###  Bar Chart")
        fig3 =  px.bar(df, y, x) 
        return st.write(fig3)

def  scatter_chart(fig_col4, df ,x, y):   
    with fig_col4:
        st.markdown("### Scatter Chart")
        fig4 =  px.scatter(df, y, x) 
        return st.write(fig4)


def line_chart(fig_col5, df ,x):
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
    fig7 = px.box(df, y="age_new", x="marital")
    return st.write(fig7)

#chamada das funções
#metricas(kpi1, kpi2, kpi3)
#density_heatmap(fig_col1,df,x,y)
#histogram(fig_col2,df,x)
#bar_chart(fig_col3,df, x,y)
#scatter_chart(fig_col4, df ,x, y)
#line_chart(fig_col5, df ,x)
#pie_chart(fig_col6, df ,x, y)
#box_chart(df,x,y)
