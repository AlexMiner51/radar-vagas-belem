import requests

FONTES = {
    "IEL": "https://carreiras.iel.org.br/PA",
    "GUPY": "https://portal.gupy.io/job-search/term=belem%20pa",
    "CIEE": "https://portal.ciee.org.br/",
    "LINKEDIN": "https://www.linkedin.com/jobs/est%C3%A1gio-jobs-bel%C3%A9m"
}

for nome, url in FONTES.items():

    try:

        resposta = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        print("=" * 50)
        print(nome)
        print("STATUS:", resposta.status_code)
        print("TAMANHO:", len(resposta.text))

    except Exception as erro:

        print("=" * 50)
        print(nome)
        print("ERRO:", erro)
