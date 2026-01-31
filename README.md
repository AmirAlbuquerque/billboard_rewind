# Billboard Rewind

Uma aplicação interativa construída com **Python + Streamlit** para explorar o ranking **Billboard Hot 100** por mês e ano, exibindo o **Top 3 em formato de pódio** e permitindo ouvir as músicas diretamente no Spotify.

---

## 🚀 Funcionalidades

- 🔥 Consulta sob demanda do Billboard Hot 100
- 📅 Filtro por mês e ano
- 🔢 Seleção da quantidade de músicas exibidas
- 🏆 Exibição do Top 3 em formato de pódio
- 🎧 Links clicáveis para ouvir no Spotify
- 🖼️ Busca automática de capa quando não fornecida pela Billboard

---

## 🧱 Estrutura do Projeto

```text
billboard_rewind/
│
├── src/
│   ├── app.py
│   │
│   │── config/
│   │   ├── page_config.py
│   │
│   ├── service/
│   │   ├── billboard_service.py
│   │   ├── deezer_service.py
│   │   ├── spotify_service.py
│   │
│   ├── ui/
│   │   ├── layout.py
│   │   ├── rankin.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Tecnologias Utilizadas

- Python 3.13
- Streamlit
- Pandas
- billboard.py
- Requests

## Instalação

### Clone o repositorio

```bash

git clone https://github.com/seu-usuario/billboard-rewind.git
cd billboard-rewind

```

### Crie e ative um ambiente virtual (Opcional)

```bash

python -m venv .venv
.venv\Scripts\activate

```

### Instale as dependências

```bash

pip install -r requirements.txt

```

### Execute a aplicação

```bash

streamlit run src/app.py

```
