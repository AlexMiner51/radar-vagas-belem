import requests

url = (
    "https://br.indeed.com/jobs"
    "?q=estagio"
    "&l=Belém%2C+PA"
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/130.0.0.0 "
        "Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Referer": "https://www.google.com/"
}

resposta = requests.get(
    url,
    headers=headers,
    timeout=30,
    allow_redirects=True
)

print("STATUS:", resposta.status_code)
print("URL FINAL:", resposta.url)
print("TAMANHO:", len(resposta.text))

print()
print(resposta.text[:3000])
