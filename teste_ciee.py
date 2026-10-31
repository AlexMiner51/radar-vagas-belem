import requests

url = (
    "https://api.ciee.org.br/vagas/"
    "vitrine-vaga/publicadas?page=1"
)

try:

    resposta = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    print("STATUS:", resposta.status_code)

    print("TEXTO INICIAL:")

    print(
        resposta.text[:3000]
    )

except Exception as erro:

    print(
        "ERRO:",
        erro
    )
