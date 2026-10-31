import requests

url = "https://portal.ciee.org.br/quero-uma-vaga/"

resposta = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("STATUS:", resposta.status_code)

print("TAMANHO:", len(resposta.text))

texto = resposta.text.lower()

print(
    "CONTÉM 'estagio'?:",
    "estagio" in texto
)

print(
    "CONTÉM 'vaga'?:",
    "vaga" in texto
)

print(
    "CONTÉM 'belém'?:",
    "belém" in texto
)

print(
    "CONTÉM 'belem'?:",
    "belem" in texto
)
