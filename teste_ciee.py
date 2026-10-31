import requests
import json

url = (
    "https://api.ciee.org.br/vagas/"
    "vitrine-vaga/publicadas?page=1"
)

dados = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
).json()

print(type(dados))

print()

print("CHAVES:")

if isinstance(dados, dict):

    for chave in dados.keys():

        print(chave)

print()

print(
    json.dumps(
        dados,
        ensure_ascii=False,
        indent=2
    )[:3000]
)
