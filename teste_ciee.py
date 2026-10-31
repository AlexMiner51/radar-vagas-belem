import requests

url = "https://portal.ciee.org.br/quero-uma-vaga/estagio/"

resposta = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

html = resposta.text.lower()

print("STATUS:", resposta.status_code)
print("TAMANHO:", len(html))

print("CONTÉM ESTAGIO:", "estagio" in html)
print("CONTÉM VAGA:", "vaga" in html)
print("CONTÉM BELÉM:", "belém" in html)
print("CONTÉM BELEM:", "belem" in html)
print("CONTÉM PARÁ:", "pará" in html)
print("CONTÉM PARA:", "para" in html)

# Procurar alguns trechos relevantes

palavras = [
    "belém",
    "belem",
    "pará",
    "para",
    "estagio",
    "vaga"
]

for palavra in palavras:

    print()
    print("====", palavra.upper(), "====")

    posicao = html.find(palavra)

    if posicao != -1:

        inicio = max(0, posicao - 100)

        fim = min(
            len(html),
            posicao + 300
        )

        print(
            html[inicio:fim]
        )

    else:

        print("NÃO ENCONTRADO")
