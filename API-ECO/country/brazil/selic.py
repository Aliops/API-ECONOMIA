from bcb import sgs
import pandas as pd
import os

def get_selic_data(start_date='2010-01-01', end_date ='2024-12-31', save_to_file=True, file_path='data/brazil/selic_data.csv'):
    """
    Importa dados da taxa SELIC a partir da API do Banco Central do Brasil (BCB) e os salva na pasta data.

    Parameters:
        start_date (str): Data de início para a coleta de dados. Formato: 'YYYY-MM-DD'.
        save_to_file (bool): Se True, salva os dados coletados em um arquivo CSV.
        file_path (str): Caminho do arquivo para salvar os dados (default: 'data/selic_data.csv').

    Returns:
        pd.DataFrame: DataFrame contendo as taxas SELIC ao longo do tempo.
    """
    try:
        # Coleta dos dados usando a API do BCB
        selic_data = sgs.get({'selic': 432}, start=start_date, end=end_date)
        selic_data.columns = ['Taxa SELIC']
        selic_data.index = pd.to_datetime(selic_data.index)

        # Salva os dados em um arquivo CSV dentro da pasta data
        if save_to_file:
            # Certifique-se de que a pasta 'data' existe
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # Salva o DataFrame como CSV
            selic_data.to_csv(file_path)
            print(f"Dados da SELIC salvos em {file_path}")
        
        return selic_data

    except Exception as e:
        print(f"Erro ao coletar dados da SELIC: {e}")
        return pd.DataFrame()

def get_or_load_selic_data(start_date='2010-01-01', end_date='2024-12-01', file_path='data/selic_data.csv', reload_data=False):
    """
    Obtém dados da taxa SELIC, seja de um arquivo local ou da API do BCB.

    Parameters:
        start_date (str): Data de início para a coleta de dados da API, se necessário.
        file_path (str): Caminho do arquivo CSV para carregar ou salvar os dados.
        reload_data (bool): Se True, recarrega os dados da API mesmo se o arquivo local existir.

    Returns:
        pd.DataFrame: DataFrame contendo as taxas SELIC ao longo do tempo.
    """
    if not reload_data and os.path.exists(file_path):
        print(f"Carregando dados da SELIC de {file_path}")
        return pd.read_csv(file_path, index_col=0, parse_dates=True)
    else:
        print("Coletando dados da SELIC da API do BCB")
        selic_data = get_selic_data(start_date=start_date, end_date=end_date, save_to_file=True, file_path=file_path)
        return selic_data