import pandas as pd
import pandas_datareader as pdr
import os

def get_fed_interest_rate(start_date='2020-01-01', end_date='2024-12-31'):
    """
    Coleta a taxa de juros do FED (Federal Funds Rate) para um período específico.
    
    Parameters:
        start_date (str): Data de início no formato 'YYYY-MM-DD'.
        end_date (str): Data de fim no formato 'YYYY-MM-DD'.
    
    Returns:
        pd.DataFrame: DataFrame contendo a taxa de juros do FED ao longo do tempo.
    """
    # Coletar dados do FRED sobre a taxa de juros do FED
    fed_rates = pdr.get_data_fred('FEDFUNDS', start=start_date, end=end_date)
    
    # Converter frequência de mensal para diária, preenchendo com o valor anterior
    fed_rates_daily = fed_rates.resample('D').ffill()
    
    return fed_rates_daily

def save_fed_interest_rate(fed_data, file_path='data/eua/fed_data.csv'):
    """
    Salva a taxa de juros do FED em um arquivo CSV.

    Parameters:
        fed_data (pd.DataFrame): Dados da taxa de juros do FED.
        file_path (str): Caminho para salvar o arquivo CSV.
    """
    # Certificar-se de que o diretório 'data/eua' existe
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Salvar dados em um arquivo CSV
    fed_data.to_csv(file_path)
    print(f"Dados da taxa de juros do FED salvos em {file_path}")

def load_fed_interest_rate(file_path='data/eua/fed_data.csv'):
    """
    Carrega a taxa de juros do FED de um arquivo CSV.

    Parameters:
        file_path (str): Caminho para carregar o arquivo CSV.
    
    Returns:
        pd.DataFrame: DataFrame contendo a taxa de juros do FED.
    """
    if os.path.exists(file_path):
        fed_data = pd.read_csv(file_path, index_col=0, parse_dates=True)
        return fed_data
    else:
        print(f"Arquivo não encontrado: {file_path}")
        return pd.DataFrame()

def get_or_load_fed_interest_rate(start_date='2010-01-01', end_date='2024-12-31', file_path='data/eua/fed_data.csv', reload_data=False):
    """
    Obtém dados da taxa de juros do FED, seja de um arquivo local ou da API do FRED.
    
    Parameters:
        start_date (str): Data de início para a coleta de dados da API, se necessário.
        end_date (str): Data de fim para a coleta de dados da API, se necessário.
        file_path (str): Caminho do arquivo CSV para carregar ou salvar os dados.
        reload_data (bool): Se True, recarrega os dados da API mesmo se o arquivo local existir.

    Returns:
        pd.DataFrame: DataFrame contendo a taxa de juros do FED ao longo do tempo.
    """
    if not reload_data and os.path.exists(file_path):
        print(f"Carregando dados da taxa de juros do FED de {file_path}")
        return load_fed_interest_rate(file_path=file_path)
    else:
        print("Coletando dados da taxa de juros do FED da API do FRED")
        fed_data = get_fed_interest_rate(start_date=start_date, end_date=end_date)
        save_fed_interest_rate(fed_data, file_path=file_path)
        return fed_data