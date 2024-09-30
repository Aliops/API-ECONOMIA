# API-ECONOMIA


# Análise e Previsão de Taxas de Juros

## Visão Geral do Projeto

Este projeto foca em analisar e prever taxas de juros do Brasil (SELIC) e dos Estados Unidos (Taxa de Juros do FED). O objetivo é fornecer uma análise interativa e visualização dessas taxas ao longo do tempo e criar previsões usando modelos ARIMA. O projeto também inclui um dashboard interativo com Streamlit para visualização de dados e previsões.

## Estrutura do Projeto

```
.
├── country/
│   ├── brazil/
│   │   ├── selic.py             # Funções para coletar e carregar dados da SELIC
│   ├── eua.py                   # Funções para coletar e carregar dados do FED
├── data/
│   ├── brazil/
│   │   ├── selic_data.csv       # Dados da SELIC (amostra)
│   ├── eua/
│   │   ├── fed_data.csv         # Dados do FED (amostra)
├── source/
│   ├── data_processing.py       # Funções para preparar e processar dados para modelagem
│   ├── initialize_data.py       # Scripts para coletar e salvar dados
│   ├── analysis.py              # Funções para visualizações e plotagens
│   ├── modeling.py              # Funções para treinar modelos e fazer previsões
│   ├── main.py                  # Script principal para executar todo o workflow de análise
│   ├── app.py                   # Aplicativo Streamlit para visualização
```

## Configuração e Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Gerenciador de pacotes `pip`

### Instalar Dependências

Instale os pacotes necessários usando o arquivo `requirements.txt` (se não fornecido, inclua os pacotes essenciais aqui):

```bash
pip install -r requirements.txt
```

Caso o `requirements.txt` não esteja disponível, instale manualmente os pacotes necessários:

```bash
pip install pandas streamlit matplotlib seaborn statsmodels pandas_datareader
```

### Coleta de Dados

Para coletar e preparar os dados, execute o script que inicializa e coleta os dados das taxas de juros para o Brasil e os EUA:

```bash
python source/initialize_data.py
```

Este script salvará os dados como arquivos CSV nos diretórios `data/brazil` e `data/eua`.

## Uso

### Executando a Análise

Para executar a análise principal, visualização e treinamento do modelo, utilize o seguinte comando:

```bash
python source/main.py
```

Este script irá:

1. Carregar e preparar dados do Brasil (SELIC) e dos EUA (FED).
2. Realizar análise comparativa e visualizações das taxas de juros.
3. Treinar modelos ARIMA para previsão das taxas de juros.
4. Avaliar as previsões dos modelos.
5. Exibir resultados e gráficos para as taxas reais e previstas.

### Executando o Dashboard

Para iniciar o dashboard interativo do Streamlit, use:

```bash
streamlit run source/app.py
```

Este dashboard permite visualizar os dados históricos, realizar análises de correlação e ver as previsões para as taxas de juros SELIC e FED.

## Descrição dos Arquivos

### `selic.py`
Contém funções para:
- Recuperar dados da SELIC de uma API ou de um arquivo local.
- Salvar e carregar dados da SELIC para processamento posterior.

### `eua.py`
Inclui funções para:
- Buscar dados da Taxa de Juros do FED da API FRED.
- Salvar e carregar os dados para uso futuro.

### `data_processing.py`
Lida com a preparação dos dados para modelagem, incluindo:
- Carregamento e limpeza de dados para o Brasil e os EUA.
- Cálculo de variações percentuais nas taxas de juros.
- Normalização dos dados para modelagem ARIMA.

### `initialize_data.py`
Um script que coleta e salva dados das taxas de juros para ambos os países, garantindo disponibilidade para análise.

### `analysis.py`
Funções para visualização de dados, incluindo:
- Plotagem de tendências das taxas de juros ao longo do tempo.
- Visualização de correlações entre as taxas SELIC e FED.
- Exibição de distribuições dos valores das taxas de juros.

### `modeling.py`
Contém funções de modelagem para:
- Treinar modelos ARIMA para previsão de séries temporais.
- Realizar previsões e avaliar a precisão do modelo.

### `main.py`
Orquestra todo o fluxo de análise por:
- Coletar, processar e visualizar dados.
- Treinar e avaliar modelos de previsão.
- Gerar e exibir visualizações para as taxas reais e previstas.

### `app.py`
Um aplicativo Streamlit que fornece:
- Uma interface interativa para explorar dados da SELIC e do FED.
- Visualizações de tendências de taxas de juros, correlações e previsões.
- Opções para definir períodos de previsão personalizados.

## Fontes de Dados

- **SELIC (Brasil)**: Dados recuperados da API do Banco Central do Brasil.
- **FED (EUA)**: Dados coletados da API FRED.


## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para mais detalhes.
