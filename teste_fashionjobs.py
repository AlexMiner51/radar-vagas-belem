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

print(
    resposta.text[:1000]
)
