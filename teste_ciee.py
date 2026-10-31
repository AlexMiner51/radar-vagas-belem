import requests

url = "https://portal.ciee.org.br/"

try:

    resposta = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    print("STATUS:", resposta.status_code)

    print("TAMANHO:", len(resposta.text))

except Exception as erro:

    print("ERRO:", erro)
