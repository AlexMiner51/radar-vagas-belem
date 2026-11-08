import requests

urls = [

    "https://www.nube.com.br/vagas",
    "https://www.nube.com.br/estagio",
    "https://www.nube.com.br/estagios",
    "https://www.nube.com.br/oportunidades",
    "https://www.nube.com.br/vagas-de-estagio",
    "https://www.nube.com.br/painel-de-vagas"

]

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/130.0.0.0 "
        "Safari/537.36"
    )
}

for url in urls:

    try:

        resposta = requests.get(
            url,
            headers=headers,
            timeout=30,
            allow_redirects=True
        )

        print()
        print("=" * 70)
        print(url)
        print("STATUS:", resposta.status_code)
        print("URL FINAL:", resposta.url)

    except Exception as erro:

        print(url)
        print("ERRO:", erro)
