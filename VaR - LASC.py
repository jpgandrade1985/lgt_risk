#!/usr/bin/env python
# coding: utf-8

# In[13]:


#setup de bibliotecas e ativo
import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

years = 3

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=365*years)

tickers = ['LASC11.SA']


# In[14]:


#busca preço de fechamento
adj_close_df = pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, start=startDate, end=endDate)
    adj_close_df[ticker] = data['Adj Close']

print(adj_close_df)


# In[15]:


#busca log retornos
log_returns = np.log(adj_close_df / adj_close_df.shift(1))
log_returns = log_returns.dropna()
print(log_returns)


# In[16]:


portfolio_value = 200000
weights = np.array([1/len(tickers)]*len(tickers))
print(weights)


# In[17]:


#retorno histórico
historical_returns = (log_returns * weights).sum(axis =1)
print(historical_returns)


# In[18]:


days = 365
range_returns = log_returns.rolling(window = days).sum()
range_returns = range_returns.dropna()
print(range_returns)


# In[19]:


confidence_interval = 0.99

VaR = -np.percentile(range_returns, 100 - (confidence_interval * 100))*portfolio_value
print(VaR)


# In[23]:


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


# In[ ]:




