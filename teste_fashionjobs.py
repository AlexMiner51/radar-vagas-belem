import requests

url = "https://br.fashionjobs.com"

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/130.0.0.0 "
        "Safari/537.36"
    ),
    "Accept": "text/html",
    "Accept-Language": "pt-BR,pt;q=0.9"
}

html = requests.get(
    url,
    headers=headers,
    timeout=30
).text.lower()

palavras = [
    "emprego",
    "vaga",
    "vagas",
    "job",
    "jobs",
    "fashionjobs",
    "belém",
    "belem"
]

for palavra in palavras:

    print()
    print("=" * 50)
    print("PALAVRA:", palavra)

    pos = html.find(palavra)

    if pos == -1:

        print("NÃO ENCONTRADA")

    else:

        inicio = max(0, pos - 200)

        fim = min(
            len(html),
            pos + 500
        )

        print(
            html[inicio:fim]
        )
