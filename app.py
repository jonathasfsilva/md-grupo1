import time
import streamlit as st
import numpy as np 
import pandas as pd 
import plotly.express as px 

st.set_page_config(
    page_title = "Teste do Streamlit por Gabriel Alves",
    layout = "wide",
    menu_items = {
        'About': "TESTE DO ABOUT"
    }
)

dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

st.title("e-commerce Dashboard")

job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

df = df[df["job"] == job_filter]

# fill in those three columns with respective metrics or KPIs

avg_age = df['age'].mean()
count_married = 10
balance = 10

kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric(
    label="Age ⏳",
    value=round(avg_age),
    delta=round(avg_age) - 10,
)

kpi2.metric(
    label="Married Count 💍",
    value=int(count_married),
    delta=-10 + count_married,
)

kpi3.metric(
    label="A/C Balance ＄",
    value=f"$ {round(balance,2)} ",
    delta=-round(balance / count_married) * 100,
)



st.write(df)


