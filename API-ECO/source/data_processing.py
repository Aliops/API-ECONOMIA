from country.brazil import get_or_load_selic_data
from country.eua import get_or_load_fed_interest_rate
import pandas as pd

def load_and_prepare_data_brazil(start_date='2020-01-01', end_date='2024-12-31', file_path='data/brazil/selic_data.csv', reload_data=False):
    """
    Carrega e prepara os dados da SELIC para modelagem.
    """
    selic_data = get_or_load_selic_data(start_date=start_date, end_date=end_date, file_path=file_path, reload_data=reload_data)
    if selic_data.empty:
        print("Os dados da SELIC não foram carregados corretamente.")
        return pd.DataFrame()
    
    # Trata dados: remove NaNs e calcula variação percentual
    selic_data = selic_data.dropna()
    selic_data['Taxa SELIC % Change'] = selic_data['Taxa SELIC'].pct_change()

    return selic_data

def load_and_prepare_data_eua(start_date='2020-01-01', end_date='2024-12-31', file_path='data/eua/fed_data.csv', reload_data=False):
    """
    Carrega e prepara os dados da taxa de juros do FED para modelagem.
    """
    fed_data = get_or_load_fed_interest_rate(start_date=start_date, end_date=end_date, file_path=file_path, reload_data=reload_data)
    if fed_data.empty:
        print("Os dados da taxa de juros do FED não foram carregados corretamente.")
        return pd.DataFrame()
    
    # Trata dados: remove NaNs e calcula variação percentual
    fed_data = fed_data.dropna()
    fed_data['Taxa FED % Change'] = fed_data['FEDFUNDS'].pct_change()

    return fed_data

def preprocess_for_modeling(data):
    """
    Pré-processa os dados para uso em modelos de previsão.
    """
    # Normaliza os dados para ter média 0 e desvio padrão 1
    data_normalized = (data - data.mean()) / data.std()
    return data_normalized
