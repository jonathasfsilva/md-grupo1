#import time  # to simulate a real time data, time loop
from turtle import xcor
import plotly.express as px  # Graficos interativos
import streamlit as st  # 🎈 web app desenvolvimento

#Comando de execução do streamlit
st.set_page_config(
    page_title="Dashboard E-commerce Olist",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded")

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


def line_chart(fig_col5, df ,y):
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


#chamada das funções
#metricas(kpi1, kpi2, kpi3)
#density_heatmap(fig_col1,df,x,y)
#histogram(fig_col2,df,x)
#bar_chart(fig_col3,df, x,y)
#scatter_chart(fig_col4, df ,x, y)
#line_chart(fig_col5, df ,x)
#pie_chart(fig_col6, df ,x, y)
#box_chart(df,x,y)
