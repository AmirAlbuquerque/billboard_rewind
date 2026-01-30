import pandas as pd
import billboard
from datetime import date, timedelta

from service.spotify_service import gerar_link_spotify

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

    dados_df = pd.DataFrame(dados)
    
    dados_df["spotify_url"] = dados_df.apply(
        lambda row: gerar_link_spotify(row['titulo'], row['artista']), axis=1
    )

    return dados_df