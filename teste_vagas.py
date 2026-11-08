import requests

url = "https://www.vagas.com.br"

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

html = requests.get(
    url,
    headers=headers,
    timeout=30
).text.lower()

palavras = [
    "vaga",
    "vagas",
    "estagio",
    "estágio",
    "emprego",
    "oportunidade",
    "oportunidades",
    "trabalheconosco",
    "busca"
]

for palavra in palavras:

    print()
    print("=" * 60)
    print("PALAVRA:", palavra)

    pos = html.find(palavra)

    if pos == -1:

        print("NAO ENCONTRADA")

    else:

        inicio = max(
            0,
            pos - 300
        )

        fim = min(
            len(html),
            pos + 700
        )

        print(html[inicio:fim])
