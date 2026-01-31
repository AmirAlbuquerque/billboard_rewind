import requests

def buscar_capa_deezer(titulo: str, artista: str) -> str | None:
    query = f"{artista} {titulo}"

    try:
        response = requests.get(
            "https://api.deezer.com/search",
            params={"q": query},
            timeout=5
        )

        if response.status_code != 200:
            return None

        data = response.json().get("data", [])
        if not data:
            return None

        album = data[0].get("album", {})
        return album.get("cover_big") or album.get("cover_medium")

    except requests.exceptions.RequestException:
        return None
