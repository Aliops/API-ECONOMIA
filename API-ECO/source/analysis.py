import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_interest_rates(df_brazil, df_eua):
    """
    Plota as taxas de juros da SELIC e do FED ao longo do tempo.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df_brazil.index, df_brazil['Taxa SELIC'], label='SELIC (Brasil)', color='blue')
    plt.plot(df_eua.index, df_eua['FEDFUNDS'], label='FED (EUA)', color='green')
    plt.title('Taxas de Juros: SELIC vs FED')
    plt.xlabel('Ano')
    plt.ylabel('Taxa (%)')
    plt.legend()
    plt.show()

def plot_correlations(df_brazil, df_eua):
    """
    Plota a correlação entre as taxas de juros da SELIC e do FED.
    """
    combined_df = pd.concat([df_brazil['Taxa SELIC'], df_eua['FEDFUNDS']], axis=1, join='inner')
    combined_df.columns = ['SELIC', 'FED']
    
    plt.figure(figsize=(8, 4))
    sns.heatmap(combined_df.corr(), annot=True, cmap='Blues')
    plt.show()

def plot_distributions(df_brazil, df_eua):
    """
    Plota distribuições das taxas SELIC e FED.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.histplot(df_brazil, x='Taxa SELIC', bins=10, ax=axes[0])
    axes[0].set_title('Distribuição da SELIC (Brasil)')
    sns.histplot(df_eua, x='FEDFUNDS', bins=10, ax=axes[1])
    axes[1].set_title('Distribuição do FED (EUA)')
    plt.tight_layout()
    plt.show()