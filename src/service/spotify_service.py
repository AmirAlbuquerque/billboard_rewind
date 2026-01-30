from urllib.parse import quote, quote_plus

def gerar_link_spotify(titulo: str, artista: str) -> str:
    query = f"{artista} {titulo}"
    # substitui espaços por hífen (padrão Spotify)
    query = query.strip().replace(" ", "-")

    # encode seguro (mantendo hífens)
    query = quote(query, safe="-")
    
    return f"https://open.spotify.com/search/{query}"
