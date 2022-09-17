# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

# read csv from DW
dim_avaliacao = pd.read_csv('data/dimAvaliacao.csv')
dim_localizacao = pd.read_csv('data/dimLocalizacao.csv')
dim_pagamento = pd.read_csv('data/dimLocalizacao.csv')
dim_produto = pd.read_csv('data/dimProduto.csv')
dim_tempo = pd.read_csv('data/dimTempo.csv')
fato_pedido = pd.read_csv('data/fatoPedido.csv')


#st.write(dim_localizacao)
#st.write(dim_pagamento)
#st.write(dim_produto)
#st.write(dim_tempo)
#st.write(fato_pedido)

# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

# dashboard title
st.title("Dashboard E-commerce Olist")
st.markdown('Este projeto apresenta o resultado da modelagem do DW em relação aos Pedidos.')

# Escolha dos filtros

with st.sidebar:
    st.header('Modelagem de Dados - Grupo 1')
    opcoes_arq = st.selectbox("Selecione os arquivos a serem consultados",('Avaliação','Tempo','Localização','Pagamento','Produto'),)
    job_filter = st.selectbox("Selecione as páginas", pd.unique(df["job"]))

if opcoes_arq == 'Tempo':
    st.write('Quantidade de pedidos realizados de acordo com os dias da semana ou final de semana')
    st.dataframe(dim_tempo)
elif opcoes_arq == 'Avaliação':
    st.write('Períodos que ocorrem maior quantidade vendas estão relacionados a datas comemorativas')
    st.dataframe(dim_avaliacao)
elif opcoes_arq == 'Localização':
    st.write('Quantidade de  categorias de pedido  vendidas por estação do ano')
    st.dataframe(dim_localizacao)
elif opcoes_arq == 'Pagamento':
    st.write('Quantidade de pedidos em relação ao de pagamento por estado')
    st.dataframe(dim_pagamento)
else:
    st.write('Média de avaliação dos pedidos por categoria de produto')
    st.dataframe(dim_produto)
