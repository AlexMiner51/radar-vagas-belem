import requests

url = "https://br.indeed.com"

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/130.0.0.0 "
        "Safari/537.36"
    ),
    "Accept": (
        "text/html,"
        "application/xhtml+xml,"
        "application/xml;q=0.9,"
        "image/avif,"
        "image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9"
}

resposta = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("STATUS:", resposta.status_code)
print("TAMANHO:", len(resposta.text))

print()
print("=" * 80)
print()

print(
    resposta.text[:2500]
)
