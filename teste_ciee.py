import requests

url = (
    "https://api.ciee.org.br/vagas/"
    "vitrine-vaga/publicadas"
    "?cityCode=1501402"
)

resposta = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("STATUS:", resposta.status_code)

print()

print(resposta.text[:3000])
