import pandas as pd
import billboard
from datetime import date, timedelta

# --------------------------------------------------
# FUNÇÃO — OBTÉM HOT-100 SOB DEMANDA
# --------------------------------------------------

def carregar_hot100(ano: int, mes: int) -> pd.DataFrame:
    # último dia do mês
    if mes == 12:
        ultimo_dia = date(ano, 12, 31)
    else:
        ultimo_dia = date(ano, mes + 1, 1) - timedelta(days=1)

    # retrocede até último sábado
    while ultimo_dia.weekday() != 5:
        ultimo_dia -= timedelta(days=1)

    chart = billboard.ChartData("hot-100", date=ultimo_dia.isoformat())
    dados = [
        {
            "rank": m.rank,
            "titulo": m.title,
            "artista": m.artist
        }
        for m in chart
    ]
    
    return pd.DataFrame(dados)