import pandas as pd
import billboard
from datetime import date, timedelta

from service.spotify_service import gerar_link_spotify
from service.deezer_service import buscar_capa_deezer

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

    dados=[]

    chart = billboard.ChartData("hot-100", date=ultimo_dia.isoformat())

    for m in chart:
        image = m.image
        if not image:
            image = buscar_capa_deezer(m.title, m.artist)
        dados.append({
                "rank": m.rank,
                "titulo": m.title,
                "artista": m.artist,
                "image": image
            })
    
    print(dados)    

    dados_df = pd.DataFrame(dados)
    if dados_df.empty:
        return pd.DataFrame(
            columns=["rank", "titulo", "artista", "image", "spotify_url"]
        )
    
    dados_df["spotify_url"] = dados_df.apply(
        lambda row: gerar_link_spotify(row['titulo'], row['artista']), axis=1
    )
    print(dados_df)

    return dados_df