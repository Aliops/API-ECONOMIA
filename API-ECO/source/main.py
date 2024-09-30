from source.data_processing import load_and_prepare_data_brazil, load_and_prepare_data_eua, preprocess_for_modeling
from source.modeling import train_arima_model, forecast_model, evaluate_model
from source.analysis import plot_interest_rates, plot_correlations, plot_distributions
import matplotlib.pyplot as plt

start_date = '2020-01-01'
end_date = '2024-12-31'

# 1. Coletar e preparar dados do Brasil (SELIC)
print("Coletando e preparando dados da SELIC (Brasil)...")
selic_data = load_and_prepare_data_brazil(start_date=start_date, end_date=end_date, file_path='data\\brazil\\selic_data.csv')
selic_data_normalized = preprocess_for_modeling(selic_data['Taxa SELIC'])

# 2. Coletar e preparar dados dos EUA (FED)
print("Coletando e preparando dados do FED (EUA)...")
fed_data = load_and_prepare_data_eua(start_date=start_date, end_date=end_date, file_path='data\\eua\\fed_data.csv')
fed_data_normalized = preprocess_for_modeling(fed_data['FEDFUNDS'])

# 3. Análise comparativa
print("Analisando e comparando as taxas de juros do Brasil e dos EUA...")
plt.figure(figsize=(10, 5))
plot_interest_rates(selic_data, fed_data)
plt.show()

plt.figure(figsize=(5, 5))
plot_correlations(selic_data, fed_data)
plt.show()

plt.figure(figsize=(10, 5))
plot_distributions(selic_data, fed_data)
plt.show()

# 4. Treinar modelos de previsão
print("Treinando modelos de previsão ARIMA...")
arima_model_brazil = train_arima_model(selic_data_normalized, order=(5, 1, 0))
arima_model_eua = train_arima_model(fed_data_normalized, order=(5, 1, 0))

# 5. Previsões usando modelos treinados
print("Fazendo previsões para o Brasil e os EUA...")
forecast_steps = 10
forecast_brazil, _ = forecast_model(arima_model_brazil, steps=forecast_steps)
forecast_eua, _ = forecast_model(arima_model_eua, steps=forecast_steps)

# 6. Avaliação de previsões
print("Avaliando previsões...")
evaluation_brazil = evaluate_model(selic_data['Taxa SELIC'][-forecast_steps:], forecast_brazil)
evaluation_eua = evaluate_model(fed_data['FEDFUNDS'][-forecast_steps:], forecast_eua)

# 7. Exibir resultados
print("\nAvaliação da Previsão - Brasil (SELIC):")
print(evaluation_brazil)

print("\nAvaliação da Previsão - EUA (FED):")
print(evaluation_eua)

# 8. Visualizar previsões
plt.figure(figsize=(10, 5))
plt.plot(selic_data.index[-forecast_steps:], selic_data['Taxa SELIC'][-forecast_steps:], label='SELIC Real', color='blue')
plt.plot(selic_data.index[-forecast_steps:], forecast_brazil, label='SELIC Prevista', color='red', linestyle='--')
plt.title('Previsão da Taxa SELIC - Brasil')
plt.xlabel('Data')
plt.ylabel('Taxa de Juros (%)')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(fed_data.index[-forecast_steps:], fed_data['FEDFUNDS'][-forecast_steps:], label='FED Real', color='green')
plt.plot(fed_data.index[-forecast_steps:], forecast_eua, label='FED Prevista', color='orange', linestyle='--')
plt.title('Previsão da Taxa FED - EUA')
plt.xlabel('Data')
plt.ylabel('Taxa de Juros (%)')
plt.legend()
plt.show()