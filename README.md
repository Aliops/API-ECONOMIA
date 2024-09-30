# API-ECONOMIA

## Análise e Previsão de Taxas de Juros

### Visão Geral

Este projeto foi desenvolvido para analisar e prever as taxas de juros do Brasil (SELIC) e dos Estados Unidos (Taxa de Juros do FED). Utilizando modelos de séries temporais (ARIMA), as taxas são analisadas ao longo do tempo e previsões são feitas com base nos dados coletados. Além disso, o projeto inclui um dashboard interativo em Streamlit para visualização dos dados e previsões.

### Estrutura do Projeto

```bash
.
├── country/
│   ├── brazil/
│   │   ├── __init__.py     
│   │   ├── selic.py             # Funções para coletar e carregar dados da SELIC
│   ├── eua/
│   │   ├── __init__.py     
│   │   ├── eua.py               # Funções para coletar e carregar dados do FED
├── data/
│   ├── brazil/
│   │   ├── selic_data.csv       # Dados coletados da SELIC
│   ├── eua/
│   │   ├── fed_data.csv         # Dados coletados do FED
├── source/
│   ├── data_processing.py       # Funções para preparar e processar dados para modelagem
│   ├── initialize_data.py       # Scripts para coleta e salvamento de dados
│   ├── analysis.py              # Funções para visualização e análise dos dados
│   ├── modeling.py              # Funções para modelagem e previsão
│   ├── main.py                  # Script principal para executar a análise completa
├── dashboard/
│   ├── app.py                   # Dashboard Streamlit para visualização interativa
├── scripts/
│   ├── initialize_data.py       # Script para coleta inicial dos dados
```

## Instalação

### Pré-requisitos

- **Python 3.8+**
- **pip** (Gerenciador de pacotes do Python)

### Instalar Dependências

Você pode instalar as dependências necessárias com o `requirements.txt`:

```bash
pip install -r requirements.txt
```

Caso o `requirements.txt` não esteja disponível, instale os pacotes manualmente:

```bash
pip install pandas streamlit matplotlib seaborn statsmodels pandas_datareader
```

## Coleta de Dados

Para coletar e preparar os dados de taxas de juros do Brasil e dos EUA, execute o script:

```bash
python scripts/initialize_data.py
```

Isso irá salvar os dados como arquivos CSV em `data/brazil` e `data/eua`.

## Uso

### Executando a Análise de Dados

Para realizar a análise, visualização e treinamento do modelo de previsão, execute:

```bash
python source/main.py
```

Isso irá:

1. Carregar e preparar os dados do Brasil (SELIC) e dos EUA (FED).
2. Realizar análise comparativa e visualização das taxas de juros.
3. Treinar modelos ARIMA para previsões.
4. Avaliar e exibir os resultados das previsões.

### Executando o Dashboard

O projeto possui um dashboard interativo desenvolvido com Streamlit. Para iniciar o dashboard e explorar os dados:

```bash
streamlit run dashboard/app.py
```

Você poderá visualizar os dados históricos, correlações e previsões das taxas de juros SELIC e FED de forma interativa.

## Detalhes dos Arquivos

- **`country/brazil/selic.py`**: Funções para coletar, carregar e salvar dados da SELIC de uma API ou arquivo local.
- **`country/eua/eua.py`**: Funções para coletar, carregar e salvar dados da Taxa de Juros do FED a partir da API FRED.
- **`source/data_processing.py`**: Processamento de dados para modelagem (limpeza, cálculos de variações percentuais e normalização).
- **`source/initialize_data.py`**: Script para coleta e salvamento de dados das taxas de juros.
- **`source/analysis.py`**: Funções para visualização e análise de dados, incluindo correlações e tendências ao longo do tempo.
- **`source/modeling.py`**: Funções para treinamento e previsão de modelos ARIMA.
- **`source/main.py`**: Executa o fluxo de análise completo, desde a coleta até a visualização e modelagem de dados.
- **`dashboard/app.py`**: Dashboard em Streamlit para visualização interativa de dados, incluindo gráficos e previsões.

## Fontes de Dados

- **SELIC (Brasil)**: Dados recuperados da API do Banco Central do Brasil.
- **FED (EUA)**: Dados coletados da API FRED (Federal Reserve Economic Data).

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
