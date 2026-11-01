import requests

url = "https://br.fashionjobs.com"

try:

    resposta = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    print("STATUS:", resposta.status_code)

    print(
        "TAMANHO:",
        len(resposta.text)
    )

except Exception as erro:

    print(
        "ERRO:",
        erro
    )
