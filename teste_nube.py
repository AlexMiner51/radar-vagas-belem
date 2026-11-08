import requests

url = "https://www.nube.com.br"

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

try:

    resposta = requests.get(
        url,
        headers=headers,
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
