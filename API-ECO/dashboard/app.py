import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from source.data_processing import load_and_prepare_data_brazil, load_and_prepare_data_eua
from source.modeling import train_arima_model, forecast_model
from source.analysis import plot_interest_rates, plot_correlations, plot_distributions

# Configuração inicial do Streamlit
st.set_page_config(page_title="Dashboard Econômico", layout="wide")

st.title("Dashboard Interativo de Taxas de Juros - Brasil & EUA")

# Inputs do usuário para as datas de início e fim
start_date = st.sidebar.date_input("Data de Início", value=pd.to_datetime('2020-01-01'))
end_date = st.sidebar.date_input("Data de Fim", value=pd.to_datetime('2024-12-01'))

# Entrada do usuário para definir o número de passos de previsão
steps_forecast = st.sidebar.number_input("Passos para Previsão", min_value=1, max_value=365, value=30)

# Seção de coleta e preparação de dados
st.header("Coleta e Preparação de Dados")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Dados Brasil - SELIC")
    selic_data = load_and_prepare_data_brazil(start_date=start_date.strftime('%Y-%m-%d'), file_path='data/brazil/selic_data.csv')
    st.dataframe(selic_data.head())

with col2:
    st.subheader("Dados EUA - FED")
    fed_data = load_and_prepare_data_eua(start_date=start_date.strftime('%Y-%m-%d'), file_path='data/eua/fed_data.csv')
    st.dataframe(fed_data.head())

# Seção de visualização de dados
st.header("Visualização de Dados")

st.subheader("Taxas de Juros ao longo do tempo")
fig, ax = plt.subplots(figsize=(10, 5))
plot_interest_rates(selic_data, fed_data)
st.pyplot(fig)

st.subheader("Correlação entre SELIC e FED")
fig, ax = plt.subplots(figsize=(5, 5))
plot_correlations(selic_data, fed_data)
st.pyplot(fig)

st.subheader("Distribuições das Taxas de Juros")
fig, ax = plt.subplots(figsize=(10, 5))
plot_distributions(selic_data, fed_data)
st.pyplot(fig)

# Seção de previsões
st.header("Previsões das Taxas de Juros")

with st.spinner("Treinando modelos..."):
    arima_model_brazil = train_arima_model(selic_data['Taxa SELIC'], order=(5, 1, 0))
    arima_model_eua = train_arima_model(fed_data['FEDFUNDS'], order=(5, 1, 0))

with st.spinner("Fazendo previsões..."):
    # Usando steps_forecast para definir o número de passos previstos
    forecast_brazil, _ = forecast_model(arima_model_brazil, steps=int(steps_forecast))
    forecast_eua, _ = forecast_model(arima_model_eua, steps=int(steps_forecast))

st.subheader(f"Previsões para {steps_forecast} dias")

# Seção de visualização das previsões
col1, col2 = st.columns(2)

with col1:
    st.write("Previsão - Brasil (SELIC)")
    st.line_chart(forecast_brazil)

with col2:
    st.write("Previsão - EUA (FED)")
    st.line_chart(forecast_eua)

st.success("Modelagem e previsões concluídas!")
