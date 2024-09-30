# Importando funções de selic.py para fácil acesso
from .selic import (
    get_selic_data,
    get_or_load_selic_data
)

# Definindo __all__ para controlar o que é exportado ao importar o pacote
__all__ = [
    'get_selic_data',
    'get_or_load_selic_data'
]