from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def train_arima_model(train_data, order=(5, 1, 0)):
    """
    Treina um modelo ARIMA nos dados de treino.
    """
    model = ARIMA(train_data, order=order)
    model_fit = model.fit()
    return model_fit

def forecast_model(model_fit, steps=10):
    """
    Faz previsões usando o modelo treinado.
    """
    forecast = model_fit.forecast(steps=steps)
    forecast_obj = model_fit.get_forecast(steps=steps)
    forecast_conf_int = forecast_obj.conf_int(alpha=0.05)
    return forecast, forecast_conf_int

def evaluate_model(test_data, forecast):
    """
    Avalia a precisão do modelo comparando a previsão com os dados reais.
    """
    evaluation_df = pd.DataFrame({
        'Data': test_data.index,
        'Valor Real': test_data,
        'Valor Previsto': forecast
    })
    return evaluation_df