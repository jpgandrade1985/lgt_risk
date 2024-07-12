#setup de bibliotecas
import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

#definição das variáveis.
#years = 3 #tamanho do histórico de preços
#portfolio_value = 200000 #valor investido no ativo
#days = 365 #para quantos dias o VaR deve calcular
#confidence_interval = 0.99 #intervalo de confiança (entre 0 e 1)

def process_data(years, portfolio_value, days, confidence_interval):

    endDate = dt.datetime.now()
    startDate = endDate - dt.timedelta(days=365*years)

    #definir ativo
    tickers = ['LASC11.SA']

    #busca preço de fechamento
    adj_close_df = pd.DataFrame()
    for ticker in tickers:
        data = yf.download(ticker, start=startDate, end=endDate)
        adj_close_df[ticker] = data['Adj Close']

    print(adj_close_df)
    #st.text('Preços de fechamento')
    #st.write(adj_close_df)

    #calcula log retornos
    log_returns = np.log(adj_close_df / adj_close_df.shift(1))
    log_returns = log_returns.dropna()
    print(log_returns)
    #st.text('Log retornos')
    #st.write(log_returns)

    #determina valor do portfólio investido no ativo
    weights = np.array([1/len(tickers)]*len(tickers))
    print(weights)

    #retorno histórico
    historical_returns = (log_returns * weights).sum(axis =1)
    print(historical_returns)
    #st.text('Retornos históricos')
    #st.write(historical_returns)

    range_returns = log_returns.rolling(window = days).sum()
    range_returns = range_returns.dropna()
    print(range_returns)

    VaR = -np.percentile(range_returns, 100 - (confidence_interval))*portfolio_value
    print(VaR)
    st.header('VaR histórico: '& VaR)

    return_window = days
    range_returns = historical_returns.rolling(window=return_window).sum()
    range_returns = range_returns.dropna()

    range_returns_dollar = range_returns * portfolio_value

    plt.hist(range_returns_dollar.dropna(), bins=50, density=True)
    plt.xlabel(f'Retorno do Portfólio {return_window} dias (R$)')
    plt.ylabel('Frequência')
    plt.title(f'Distribuição dos retornos do Portfólio - {return_window} dias (em R$)')
    plt.axvline(-VaR, color='r', linestyle='dashed', linewidth=2, label=f'VaR - Intervalo de confiança {confidence_interval:.0%}')
    plt.legend()
    plt.show()
    
    col1, col2, col3 = st.columns(3)

    with col1:
       st.markdown("preços de fechamento")
       st.write(adj_close_df)

    with col2:
       st.markdown("Log retornos")
       st.write(log_returns)
    
    with col3:
       st.markdown("retornos históricos")
       st.write(historical_returns)

with st.form(key='input_var_data'):
    years = st.number_input('Tamanho do histórico (anos) - Sugestão: 3', step=1)
    portfolio_value = st.number_input('Valor Investido', step=1)
    days = st.number_input('Dias de var. Sugestão: 365 ', step=1)
    confidence_interval = st.number_input('Intervalo de Confiança:', step=1)
    submit_button = st.form_submit_button(label='Submit')

# Use the input data
if submit_button:
    result = process_data(years, portfolio_value, days, confidence_interval)
    st.write(result)
