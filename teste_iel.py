import requests

html = requests.get(
    "https://carreiras.iel.org.br/PA",
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

for linha in html.splitlines():

    if "belem" in linha.lower():
        print(linha)

    if "belém" in linha.lower():
        print(linha)

    if "belem-pa" in linha.lower():
        print(linha)

    if "belem-pa" in linha.lower():
        print(linha)
