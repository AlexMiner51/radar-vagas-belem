import requests
import json

url = (
    "https://api.ciee.org.br/core/city/search"
    "?filter=belem"
)

resposta = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("STATUS:", resposta.status_code)

try:

    dados = resposta.json()

    print(
        json.dumps(
            dados,
            ensure_ascii=False,
            indent=2
        )[:5000]
    )

except Exception:

    print(
        resposta.text[:5000]
    )
