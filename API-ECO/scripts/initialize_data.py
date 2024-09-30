import pandas as pd
from source.data_processing import load_and_prepare_data_brazil, load_and_prepare_data_eua

# Definir o período para a coleta de dados
start_date = '2020-01-01'
end_date = '2024-12-31'

# Caminhos dos arquivos CSV onde os dados serão salvos
brazil_file_path = 'data/brazil/selic_data.csv'
eua_file_path = 'data/eua/fed_data.csv'

# Função para coletar e salvar dados da SELIC (Brasil)
def save_brazil_data():
    print("Coletando dados da SELIC (Brasil)...")
    # Coleta e prepara os dados
    selic_data = load_and_prepare_data_brazil(
        start_date=start_date, 
        end_date=end_date, 
        file_path=brazil_file_path, 
        reload_data=True  # Recarrega dados mesmo se o arquivo já existir
    )
    
    # Verifica se os dados foram coletados corretamente
    if not selic_data.empty:
        selic_data.to_csv(brazil_file_path, index=False)
        print(f"Dados da SELIC salvos em {brazil_file_path}")
    else:
        print("Erro: Não foi possível coletar os dados da SELIC.")

# Função para coletar e salvar dados do FED (EUA)
def save_eua_data():
    print("Coletando dados da taxa de juros do FED (EUA)...")
    # Coleta e prepara os dados
    fed_data = load_and_prepare_data_eua(
        start_date=start_date, 
        end_date=end_date, 
        file_path=eua_file_path, 
        reload_data=True  # Recarrega dados mesmo se o arquivo já existir
    )
    
    # Verifica se os dados foram coletados corretamente
    if not fed_data.empty:
        fed_data.to_csv(eua_file_path, index=False)
        print(f"Dados do FED salvos em {eua_file_path}")
    else:
        print("Erro: Não foi possível coletar os dados do FED.")

# Ponto de entrada principal do script
if __name__ == '__main__':
    # Coleta e salva dados para ambos os países
    save_brazil_data()
    save_eua_data()
    print("Dados salvos com sucesso!")